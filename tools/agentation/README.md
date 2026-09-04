# Agentation (dev-only)

`agentation.js` is the Agentation 3.0.2 feedback toolbar bundled with React 18
into one script (esbuild, IIFE). `index.html` and `dashboard.html` load it only
when the page is served from localhost / 127.0.0.1, so it never runs in
production; `tools/` is also in `.vercelignore`, so the file never uploads.

It syncs annotations to the agentation-mcp HTTP server on http://localhost:4747.
Start that with:

    npx -y agentation-mcp server

The same command is registered with Claude Code as the `agentation` MCP server
(local scope, this project), so a fresh Claude Code session starts it itself.

Rebuild (from a scratch dir with esbuild, agentation, react@18, react-dom@18):

    npx esbuild entry.jsx --bundle --format=iife --platform=browser \
      --target=es2020 --minify --define:process.env.NODE_ENV='"development"' \
      --outfile=agentation.js
