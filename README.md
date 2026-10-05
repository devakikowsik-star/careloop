# CareLoop

CareLoop turns doorbell and motion events into one short, clear message for families whose parents live alone.

## The problem
Adults living far from their parents worry daily but have no easy way to know whether the parent is okay. Phone calls rely on the parent saying "I'm fine", and raw camera or doorbell alerts are too noisy to review. CareLoop turns many small events into one sentence a family can understand in 10 seconds, such as "4 events today. Normal day." or "Please check on your parent."

## How it works
- `ring_source.py`: provides simulated home events (doorbell and motion)
- `rules.py`: plain code that finds the longest quiet period and decides "normal" or "alert" (no AI makes the safety decision)
- `summary.py`: builds the short message
- `tools.py`: four functions that answer family questions
- `mcp_server.py`: an MCP server (Streamable HTTP) that exposes those four functions as tools to an assistant such as Alexa+
- `chat_app.py`: a simulated Alexa+ chat page that calls the same tools

## Alexa+ track
- Self-hosted MCP server using Streamable HTTP
- Tools: get_today_summary, get_last_visitor, is_everything_ok, get_last_activity_time

## Important: the data is simulated
All home events are fake and generated in `ring_source.py`. This project does not connect to a real Ring device or to any real person's home. It is not an emergency service.

## Run it
1. Install Python 3.11 or newer
2. `python -m venv venv` then `venv\Scripts\activate`
3. `pip install streamlit "mcp[cli]<2"`
4. MCP server: `python mcp_server.py` (runs at http://127.0.0.1:8000/mcp)
5. Test the tools with MCP Inspector: `npx @modelcontextprotocol/inspector`, choose Streamable HTTP, enter the URL above
6. Chat simulation: `streamlit run chat_app.py`

## Built with
Python, Streamlit, MCP Python SDK (FastMCP, version 1.x)

## Demo video
[paste your YouTube link here later]

## Friction log
See friction-log.md

## License
MIT