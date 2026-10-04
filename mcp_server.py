from mcp.server.fastmcp import FastMCP
from ring_source import get_events
from rules import check_day
from summary import make_summary

mcp = FastMCP("careloop")


@mcp.tool()
def get_today_summary(scenario: str = "normal") -> str:
    """Give a short summary of today's activity at the parent's home."""
    events = get_events(scenario)
    result = check_day(events)
    return make_summary(events, result)


@mcp.tool()
def get_last_visitor(scenario: str = "normal") -> str:
    """Tell who last rang the doorbell today."""
    events = get_events(scenario)
    for e in reversed(events):
        if e["type"] == "doorbell":
            return f"The last doorbell was at {e['time']}: {e['note']}."
    return "No one has rung the doorbell today."


if __name__ == "__main__":
    mcp.run(transport="streamable-http")