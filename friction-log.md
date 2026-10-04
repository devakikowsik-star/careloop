# Friction log

## Setup
- Streamlit asked for an email on first run (skipped with Enter)
- pip showed an update notice (harmless)

## MCP library
- Task: run a FastMCP server
- Expected: `pip install "mcp[cli]"` then `from mcp.server.fastmcp import FastMCP` works
- Actual: installed mcp 2.x, import failed because FastMCP was renamed
- Workaround: `pip install "mcp[cli]<2"` (installed 1.30.0)
- Suggestion: docs and samples should state the required mcp version

## MCP Inspector 2.9.0
- Expected: a form to enter the server URL
- Actual: a server list; the Add server form defaults to stdio, and I had to switch to Streamable HTTP

## Ring API (research)
- Ring track needs a Ring account with a Ring Protection plan, and the docs say only US-located devices are supported
- Needs public HTTPS endpoints and OAuth, which is hard for a beginner
- The hackathon page says no device is needed, but the Ring docs describe testing with real accounts. I could not find a simulator
- Decision: entered the Alexa+ track instead