"""Factory PRDCT-20052 public fixture: a tiny FastMCP server (never executed by the scanner)."""
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("factory-public-fixture")


@mcp.tool()
def read_note(name: str) -> str:
    """Read a note by name."""
    return f"note {name}"


@mcp.tool(name="list_notes", description="List all notes")
def list_notes() -> list[str]:
    return []


if __name__ == "__main__":
    mcp.run()
