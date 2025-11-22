from mcp.server.fastmcp import FastMCP
from app.rag.pipeline import RAGPipeline



app = FastMCP("unicourse-mcp")
pipeline = RAGPipeline()

@app.tool()
def ask_course(query: str) -> str:
    """
    MCP tool to ask questions about courses.
    """
    answer = pipeline.ask(query)
    return answer

if __name__ == "__main__":
    app.run()
