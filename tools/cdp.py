"""Minimal stdlib-only Chrome DevTools Protocol client.

Launches headless Chrome (--headless=new), opens a page, and evaluates
JavaScript in it. No third-party packages, no npm install.

    from cdp import Chrome
    with Chrome(width=1024) as c:
        c.goto("file:///path/index.html")
        print(c.eval("antz.checkDefaults()"))
        print(c.console)          # anything the page logged or threw
"""
import base64, hashlib, json, os, re, socket, struct, subprocess, sys, tempfile, time, urllib.request

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"


class WS:
    """Just enough RFC 6455 to talk to Chrome: text frames, client-masked."""

    def __init__(self, url):
        m = re.match(r"ws://([^:/]+):(\d+)(/.*)", url)
        host, port, path = m.group(1), int(m.group(2)), m.group(3)
        self.sock = socket.create_connection((host, port))
        self.sock.settimeout(30)
        key = base64.b64encode(os.urandom(16)).decode()
        self.sock.sendall(
            f"GET {path} HTTP/1.1\r\nHost: {host}:{port}\r\nUpgrade: websocket\r\n"
            f"Connection: Upgrade\r\nSec-WebSocket-Key: {key}\r\n"
            f"Sec-WebSocket-Version: 13\r\n\r\n".encode()
        )
        buf = b""
        while b"\r\n\r\n" not in buf:
            buf += self.sock.recv(4096)
        status = buf.split(b"\r\n", 1)[0]
        assert b"101" in status, f"websocket handshake rejected: {status!r}"
        self.buf = buf.split(b"\r\n\r\n", 1)[1]

    def send(self, obj):
        payload = json.dumps(obj).encode()
        n = len(payload)
        head = b"\x81"
        if n < 126:
            head += bytes([0x80 | n])
        elif n < 1 << 16:
            head += bytes([0x80 | 126]) + struct.pack(">H", n)
        else:
            head += bytes([0x80 | 127]) + struct.pack(">Q", n)
        mask = os.urandom(4)
        self.sock.sendall(head + mask + bytes(b ^ mask[i % 4] for i, b in enumerate(payload)))

    def _read(self, n):
        while len(self.buf) < n:
            chunk = self.sock.recv(65536)
            if not chunk:
                raise EOFError("chrome closed the connection")
            self.buf += chunk
        out, self.buf = self.buf[:n], self.buf[n:]
        return out

    def recv(self):
        while True:
            b0, b1 = self._read(2)
            opcode, n = b0 & 0x0F, b1 & 0x7F
            if n == 126:
                n = struct.unpack(">H", self._read(2))[0]
            elif n == 127:
                n = struct.unpack(">Q", self._read(8))[0]
            data = self._read(n)
            if opcode == 0x8:                      # close
                raise EOFError("chrome closed the socket")
            if opcode == 0x9:                      # ping -> pong
                self.sock.sendall(b"\x8a" + bytes([len(data)]) + data)
                continue
            if opcode in (0x1, 0x2):
                return json.loads(data)

    def close(self):
        try:
            self.sock.close()
        except OSError:
            pass


class Chrome:
    def __init__(self, width=1024, height=1400, port=9333, reduced_motion=True):
        self.width, self.height, self.port = width, height, port
        self.profile = tempfile.mkdtemp(prefix="cdp-profile-")
        args = [
            CHROME, "--headless=new", f"--remote-debugging-port={port}",
            f"--user-data-dir={self.profile}", "--no-first-run", "--no-default-browser-check",
            "--disable-gpu", "--hide-scrollbars", "--allow-file-access-from-files",
            f"--window-size={width},{height}", "about:blank",
        ]
        if reduced_motion:
            args.insert(-1, "--force-prefers-reduced-motion")
        self.proc = subprocess.Popen(args, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        target = None
        for _ in range(100):
            try:
                pages = json.load(urllib.request.urlopen(f"http://127.0.0.1:{port}/json"))
                target = next(p for p in pages if p["type"] == "page")
                break
            except Exception:
                time.sleep(0.1)
        if not target:
            raise RuntimeError("chrome did not come up")
        self.ws = WS(target["webSocketDebuggerUrl"])
        self.id = 0
        self.console = []
        self.cmd("Runtime.enable")
        self.cmd("Page.enable")
        self.cmd("Log.enable")
        self.set_viewport(width, height)

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        self.quit()

    def cmd(self, method, **params):
        self.id += 1
        mid = self.id
        self.ws.send({"id": mid, "method": method, "params": params})
        while True:
            msg = self.ws.recv()
            if msg.get("method") == "Runtime.consoleAPICalled":
                a = msg["params"]["args"]
                self.console.append(
                    (msg["params"]["type"], " ".join(str(x.get("value", x.get("description", "?"))) for x in a))
                )
            elif msg.get("method") == "Runtime.exceptionThrown":
                d = msg["params"]["exceptionDetails"]
                self.console.append(("exception", d.get("text", "") + " " + str(d.get("exception", {}).get("description", ""))))
            elif msg.get("method") == "Log.entryAdded":
                e = msg["params"]["entry"]
                if e["level"] in ("error", "warning"):
                    self.console.append((e["level"], e["text"]))
            elif msg.get("id") == mid:
                if "error" in msg:
                    raise RuntimeError(f"{method}: {msg['error']}")
                return msg.get("result", {})

    def set_viewport(self, width, height):
        self.width, self.height = width, height
        self.cmd("Emulation.setDeviceMetricsOverride",
                 width=width, height=height, deviceScaleFactor=1, mobile=False)

    def goto(self, url, settle=0.8):
        self.cmd("Page.navigate", url=url)
        deadline = time.time() + 20
        while time.time() < deadline:
            try:
                if self.eval("document.readyState") == "complete":
                    break
            except RuntimeError:
                pass
            time.sleep(0.1)
        time.sleep(settle)

    def eval(self, expr, await_promise=False):
        r = self.cmd("Runtime.evaluate", expression=expr, returnByValue=True,
                     awaitPromise=await_promise, userGesture=True)
        if "exceptionDetails" in r:
            d = r["exceptionDetails"]
            raise RuntimeError(d.get("text", "") + " " + str(d.get("exception", {}).get("description", "")))
        return r["result"].get("value")

    # ── real input ─────────────────────────────────────────────────────────
    # A synthesised PointerEvent cannot hold pointer capture: it starts a drag
    # and then never reorders anything, which reads as a product bug and is not.
    # Everything below goes through the browser's own input pipeline instead.

    def _mouse(self, kind, x, y, buttons=0):
        self.cmd("Input.dispatchMouseEvent", type=kind, x=x, y=y, button="left",
                 buttons=buttons, clickCount=1 if kind != "mouseMoved" else 0)

    def centre(self, selector):
        """Viewport centre of the first match, or None if it isn't on screen."""
        return self.eval(
            f"(()=>{{const e=document.querySelector({json.dumps(selector)});if(!e)return null;"
            "const r=e.getBoundingClientRect();"
            "return {x:r.left+r.width/2,y:r.top+r.height/2,w:r.width,h:r.height}})()"
        )

    def drag(self, from_sel, to_sel, steps=24, hold=0.12):
        """Press on one element, travel to another, release — real mouse input."""
        a, b = self.centre(from_sel), self.centre(to_sel)
        if not a or not b:
            raise RuntimeError(f"drag: missing {from_sel if not a else to_sel}")
        self._mouse("mouseMoved", a["x"], a["y"])
        self._mouse("mousePressed", a["x"], a["y"], buttons=1)
        time.sleep(hold)
        for i in range(1, steps + 1):
            t = i / steps
            self._mouse("mouseMoved", a["x"] + (b["x"] - a["x"]) * t,
                        a["y"] + (b["y"] - a["y"]) * t, buttons=1)
            time.sleep(0.016)
        time.sleep(hold)
        self._mouse("mouseReleased", b["x"], b["y"])
        time.sleep(0.4)

    def touch_drag(self, from_sel, to_sel, steps=24, hold=0.35):
        """The same journey as a finger.

        The hold is longer than the mouse's on purpose: the grid makes a finger
        stay still for TOUCH_HOLD_MS (200ms) within TOUCH_SLOP (8px) before a
        press becomes a drag, so that a swipe still scrolls the page. Move
        sooner than that and the card never lifts — which looks exactly like a
        broken drag and is not one.
        """
        a, b = self.centre(from_sel), self.centre(to_sel)
        if not a or not b:
            raise RuntimeError(f"touch_drag: missing {from_sel if not a else to_sel}")

        def point(x, y):
            return [{"x": x, "y": y, "radiusX": 8, "radiusY": 8, "force": 1}]

        self.cmd("Input.dispatchTouchEvent", type="touchStart", touchPoints=point(a["x"], a["y"]))
        time.sleep(hold)
        for i in range(1, steps + 1):
            t = i / steps
            self.cmd("Input.dispatchTouchEvent", type="touchMove",
                     touchPoints=point(a["x"] + (b["x"] - a["x"]) * t,
                                       a["y"] + (b["y"] - a["y"]) * t))
            time.sleep(0.016)
        time.sleep(hold)
        self.cmd("Input.dispatchTouchEvent", type="touchEnd", touchPoints=[])
        time.sleep(0.4)

    def click(self, selector):
        p = self.centre(selector)
        if not p:
            raise RuntimeError(f"click: missing {selector}")
        self._mouse("mouseMoved", p["x"], p["y"])
        self._mouse("mousePressed", p["x"], p["y"], buttons=1)
        self._mouse("mouseReleased", p["x"], p["y"])
        time.sleep(0.25)

    def screenshot(self, path):
        data = self.cmd("Page.captureScreenshot", format="png", captureBeyondViewport=True)["data"]
        with open(path, "wb") as f:
            f.write(base64.b64decode(data))
        return path

    def errors(self):
        return [c for c in self.console if c[0] in ("error", "exception")]

    def quit(self):
        try:
            self.ws.close()
        finally:
            self.proc.terminate()
            try:
                self.proc.wait(timeout=5)
            except subprocess.TimeoutExpired:
                self.proc.kill()
