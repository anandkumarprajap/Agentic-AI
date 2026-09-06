import subprocess
# Capitalised to ChatOllama so Python can map the library properly
from langchain_ollama import ChatOllama as chatollama 
# Standardized modern agent engine factory
from langchain.agents import create_agent 
from langchain_core.tools import tool

# --- 1. DEFINE TOOLS FIRST (With required docstrings) ---

@tool
def show_running_containers():
    """Shows a list of all currently running Docker containers."""
    result = subprocess.run(["docker", "ps"], capture_output=True, text=True)
    return result.stdout

@tool
def show_docker_logs(container_name: str):
    """Retrieves the logs of a specific Docker container using its name or ID."""
    result = subprocess.run(["docker", "logs", container_name], capture_output=True, text=True)
    return result.stdout

# --- 2. CONFIGURATION & INITIALIZATION ---

SYSTEM_PROMPT = """
You are a Docker Expert. You can explain things in 1-2 lines max.
You don't overthink, hallucinate or keep reasoning in a loop.
You Reason and Act according to user prompt
these are the things you do:
1/ You tell about errors (what went wrong, etc)
2/ You tell about the root cause (What was the cause likely)
3/ You tell about the fix or solution in short"""

model = chatollama(
    model="gemma4:12b", 
    temperature=0
)

tools = [show_running_containers, show_docker_logs]

# --- 3. AGENT DEFINITION ---
# Fixed: create_agent uses the 'system_prompt' keyword parameter instead of state_modifier
agent = create_agent(
    model=model, 
    tools=tools, 
    system_prompt=SYSTEM_PROMPT
) 

# --- 4. EXECUTION ---

# subprocess.run(["docker", "ps"])

# while True:
#     user_input = input("User:")
#     if user_input == "exit":
#         break

response = agent.invoke(
    { 
        "messages": [
            {"role": "user", "content": "How do i fix permission denied error in docker?"}
        ] 
    }
)

# Print the clean textual response down onto your console screen
print(response['messages'][-1].content)
