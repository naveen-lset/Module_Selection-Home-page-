/**
 * GRAB FRAMES · read an iPhone screen recording that Chrome cannot open
 * ───────────────────────────────────────────────────────────────────────────
 * The recordings in References/ are HEVC. Headless Chrome reports their
 * duration and then decodes nothing — `videoWidth` stays 0, no error is
 * raised, and a canvas grab silently returns a blank frame. AVFoundation
 * decodes them, so this does, with no third-party anything.
 *
 *     swiftc -O -o tools/grab_frames tools/grab_frames.swift
 *     tools/grab_frames <video> <out-dir> <prefix> 2,4,6.5,8
 *
 * Frames land as <out-dir>/<prefix>_<seconds>.png, longest side 1040. Build a
 * contact sheet out of them (an HTML grid + tools/cdp.py screenshot) rather
 * than reading forty PNGs one at a time.
 *
 * Tolerances are zero on both sides of the requested time: a frame asked for
 * at 5.4s IS the frame at 5.4s, which is the whole point when the thing being
 * measured is a 400ms transition.
 */
import Foundation
import AVFoundation
import AppKit

let args = CommandLine.arguments
let url = URL(fileURLWithPath: args[1])
let outDir = args[2]
let prefix = args[3]
let times: [Double] = args[4].split(separator: ",").map { Double($0)! }

let asset = AVURLAsset(url: url)
let gen = AVAssetImageGenerator(asset: asset)
gen.appliesPreferredTrackTransform = true
gen.requestedTimeToleranceBefore = .zero
gen.requestedTimeToleranceAfter = .zero
gen.maximumSize = CGSize(width: 480, height: 1040)

for t in times {
    let time = CMTime(seconds: t, preferredTimescale: 600)
    do {
        let cg = try gen.copyCGImage(at: time, actualTime: nil)
        let rep = NSBitmapImageRep(cgImage: cg)
        guard let data = rep.representation(using: .png, properties: [:]) else { continue }
        let name = String(format: "%@_%06.2f.png", prefix, t)
        try data.write(to: URL(fileURLWithPath: outDir + "/" + name))
        print("ok \(name) \(cg.width)x\(cg.height)")
    } catch {
        print("fail \(t): \(error)")
    }
}
