from mcp.server.fastmcp import FastMCP
import tools

mcp = FastMCP("careloop")


@mcp.tool()
def get_today_summary(scenario: str = "normal") -> str:
    """Give a short summary of today's activity at the parent's home."""
    return tools.today_summary(scenario)


@mcp.tool()
def get_last_visitor(scenario: str = "normal") -> str:
    """Tell who last rang the doorbell today."""
    return tools.last_visitor(scenario)


@mcp.tool()
def is_everything_ok(scenario: str = "normal") -> str:
    """Say whether today looks normal or whether the family should check in."""
    return tools.is_everything_ok(scenario)


@mcp.tool()
def get_last_activity_time(scenario: str = "normal") -> str:
    """Tell when something last happened at the home today."""
    return tools.last_activity_time(scenario)


if __name__ == "__main__":
    mcp.run(transport="streamable-http")