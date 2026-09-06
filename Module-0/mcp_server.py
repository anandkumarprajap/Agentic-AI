from fastmcp import FastMCP 
import subprocess

mcp = FastMCP("docker mcp server")

@mcp.tool
def show_running_containers():
    """Shows a list of all currently running Docker containers."""
    result = subprocess.run(["docker", "ps"], capture_output=True, text=True)
    return result.stdout

@mcp.tool
def show_docker_logs(container_name: str):
    """Retrieves the logs of a specific Docker container using its name or ID."""
    result = subprocess.run(["docker", "logs", container_name], capture_output=True, text=True)
    return result.stdout

if __name__ == "__main__":
    mcp.run()