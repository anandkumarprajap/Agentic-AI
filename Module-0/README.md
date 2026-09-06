# 🐍 Agentic AI + MCP — Complete Environment Setup

A complete Windows PowerShell setup guide for building an **Agentic AI application** using:

* 🐍 Python
* 🦜 LangChain
* 🧠 LangGraph
* 🦙 Ollama
* 🤖 Gemma / Qwen
* 🔌 MCP
* ⚡ FastMCP
* 🔗 LangChain MCP Adapters

---

## 📋 Table of Contents

1. [Create the Project](#1--create-the-project)
2. [Activate Virtual Environment](#2--activate-virtual-environment)
3. [Deactivate Environment](#3--deactivate-environment)
4. [Upgrade pip](#4--upgrade-pip)
5. [Install Python Packages](#5--install-python-packages)
6. [Save Dependencies](#6--save-dependencies)
7. [Install Ollama](#7--install-ollama)
8. [Download an LLM](#8--download-an-llm)
9. [Test Ollama Directly](#9--test-ollama-directly)
10. [Understand the Architecture](#10--understand-the-architecture)
11. [First LangChain + Ollama Test](#11--first-langchain--ollama-test)
12. [First LangGraph Test](#12--first-langgraph-test)
13. [MCP Server](#13--mcp-server)
14. [Agent + MCP Concept](#14--agent--mcp-concept)
15. [Check Everything](#15--check-everything)
16. [Recommended Project Structure](#16--recommended-project-structure)
17. [Complete Setup Sequence](#17--complete-setup-sequence)
18. [Most Important Mental Model](#-the-most-important-mental-model)

---

# 1. 📁 Create the Project

Open **PowerShell**.

Create the project directory:

```powershell
mkdir "X:\Agentic Ai"
cd "X:\Agentic Ai"
```

Create a Python virtual environment:

```powershell
python -m venv venv
```

Your initial project will look like:

```text
X:\Agentic Ai\
│
├── venv\
│
├── agent_mcp.py
├── mcp_server.py
├── requirements.txt
└── README.md
```

---

# 2. 🐍 Activate Virtual Environment

In PowerShell, allow script execution for the current PowerShell process:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

Activate the virtual environment:

```powershell
.\venv\Scripts\Activate.ps1
```

If successful, you should see something similar to:

```text
(venv) PS X:\Agentic Ai>
```

## Verify Python

Check the Python version:

```powershell
python --version
```

Check which Python executable is being used:

```powershell
where.exe python
```

It should point to something similar to:

```text
X:\Agentic Ai\venv\Scripts\python.exe
```

---

# 3. ⛔ Deactivate Environment

Whenever you want to leave the virtual environment:

```powershell
deactivate
```

To activate it again:

```powershell
.\venv\Scripts\Activate.ps1
```

---

# 4. 📦 Upgrade pip

Make sure the virtual environment is activated.

Upgrade `pip`:

```powershell
python -m pip install --upgrade pip
```

Check the installed version:

```powershell
pip --version
```

---

# 5. 📦 Install Python Packages

Install the required packages:

```powershell
pip install langchain langchain-ollama langgraph fastmcp langchain-mcp-adapters
```

## 📦 Package Responsibilities

| Package                  | Purpose                                            |
| ------------------------ | -------------------------------------------------- |
| `langchain`              | Framework for building LLM applications and agents |
| `langchain-ollama`       | Connects LangChain with Ollama                     |
| `langgraph`              | Builds agent workflows and stateful agent systems  |
| `fastmcp`                | Framework for creating MCP servers                 |
| `langchain-mcp-adapters` | Connects MCP tools with LangChain/LangGraph        |

### ⚠️ Important Package Name

The package name is:

```text
langchain-mcp-adapters
```

Notice the **`s`** at the end.

Do not use:

```text
langchain-mcp-adapter
```

Use:

```text
langchain-mcp-adapters
```

---

# 6. 📋 Save Dependencies

After installing the packages, save the installed dependencies:

```powershell
pip freeze > requirements.txt
```

Later, you can reinstall all dependencies with:

```powershell
pip install -r requirements.txt
```

## Check Installed Packages

List all installed packages:

```powershell
pip list
```

Or check individual packages:

```powershell
pip show langchain
pip show langchain-ollama
pip show langgraph
pip show fastmcp
pip show langchain-mcp-adapters
```

---

# 7. 🦙 Install Ollama

Ollama itself is **not installed using pip**.

Install Ollama for Windows from the official website:

**Ollama:** https://ollama.com/

After installation, open a **new PowerShell window**.

Check the installation:

```powershell
ollama --version
```

You should see the installed Ollama version.

---

# 8. 🧠 Download an LLM

You can download a local LLM using Ollama.

For example:

```powershell
ollama pull gemma4:12b
```

Or:

```powershell
ollama pull qwen2.5
```

Check the models installed on your computer:

```powershell
ollama list
```

Example:

```text
NAME           SIZE
gemma4:12b     ...
qwen2.5        ...
```

> **Note:** The exact model names and tags available in Ollama can change. Use `ollama list` to see what is actually installed.

---

# 9. 🧪 Test Ollama Directly

Before writing Python code, make sure Ollama itself works.

Run:

```powershell
ollama run gemma4:12b
```

Then ask:

```text
What is artificial intelligence?
```

If the model responds, your:

```text
Ollama
   +
LLM
```

installation is working.

Exit the interactive Ollama session:

```text
/bye
```

---

# 10. 🔌 Understand the Architecture

Your Agentic AI application will eventually look like this:

```text
                    YOUR AGENT
                        │
                        ▼
                  LangGraph
                        │
                        ▼
                   LangChain
                        │
             ┌──────────┴──────────┐
             │                     │
             ▼                     ▼
        Ollama LLM             MCP Tools
             │                     │
             ▼                     ▼
        Gemma / Qwen          MCP Server
                                   │
                         ┌─────────┼─────────┐
                         ▼         ▼         ▼
                       Tool 1    Tool 2    Tool 3
```

The responsibilities can be understood as follows.

---

## 🦙 Ollama

**Ollama runs the actual local LLM.**

```text
Ollama
   ↓
Gemma / Qwen / Other Model
```

Ollama provides the runtime for running local language models.

---

## 🦜 LangChain

**LangChain helps your Python application communicate with the LLM and tools.**

```text
Python
  ↓
LangChain
  ↓
Ollama
  ↓
LLM
```

---

## 🧠 LangGraph

**LangGraph controls the workflow and state of an agent.**

A simple workflow can look like:

```text
START
  ↓
Agent
  ↓
Think
  ↓
Tool?
 ├── Yes → Tool → Agent
 └── No  → END
```

LangGraph becomes particularly useful when an agent has:

* Multiple steps
* Tools
* Decisions
* Loops
* State
* Conditional workflows

---

## 🔌 MCP

**MCP (Model Context Protocol) standardizes how an AI application can discover and use external tools and data.**

```text
AI Application
      │
      │ MCP
      ▼
 MCP Server
      │
 ┌────┼────┐
 ▼    ▼    ▼
Tool Tool Resource
```

MCP is the communication/protocol layer between an AI application and MCP-compatible servers.

---

## ⚡ FastMCP

**FastMCP is a Python framework for creating MCP servers more easily.**

It allows you to define tools using Python functions.

For example:

```python
@mcp.tool
def add_numbers(a: int, b: int) -> int:
    return a + b
```

---

# 11. 🧪 First LangChain + Ollama Test

Create the file:

```text
agent_mcp.py
```

Add the following code:

```python
from langchain_ollama import ChatOllama


llm = ChatOllama(
    model="gemma4:12b",
    temperature=0
)


response = llm.invoke(
    "Explain Agentic AI in simple words."
)


print(response.content)
```

Run:

```powershell
python .\agent_mcp.py
```

The expected flow is:

```text
Python
  ↓
LangChain
  ↓
langchain-ollama
  ↓
Ollama
  ↓
Gemma 4
  ↓
Response
```

If you receive a response from the model, the basic **LangChain + Ollama** connection is working.

---

# 12. 🧠 First LangGraph Test

Now introduce LangGraph.

> **Note:** This is a separate LangGraph test from the LangChain + Ollama example above.

Example:

```python
from typing import TypedDict

from langgraph.graph import StateGraph, START, END


class AgentState(TypedDict):
    message: str


def process_message(state: AgentState):
    return {
        "message": state["message"] + " -> processed"
    }


graph = StateGraph(AgentState)

graph.add_node("process", process_message)

graph.add_edge(START, "process")
graph.add_edge("process", END)

app = graph.compile()


result = app.invoke({
    "message": "Hello Agent"
})


print(result)
```

Run:

```powershell
python .\agent_mcp.py
```

The important concept is:

```text
START
  ↓
process
  ↓
END
```

LangGraph becomes useful when your application needs a more complex workflow involving:

```text
State
  ↓
Decision
  ↓
Tool
  ↓
Observation
  ↓
Another Decision
  ↓
Final Answer
```

---

# 13. 🔧 MCP Server

Create:

```text
mcp_server.py
```

Add the following FastMCP server:

```python
from fastmcp import FastMCP


mcp = FastMCP("My MCP Server")


@mcp.tool
def add_numbers(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


@mcp.tool
def greet(name: str) -> str:
    """Greet a user."""
    return f"Hello, {name}!"


if __name__ == "__main__":
    mcp.run()
```

You have now created an MCP server containing two tools:

```text
MCP Server
    │
    ├── add_numbers()
    │
    └── greet()
```

### Tool 1 — `add_numbers`

```python
add_numbers(10, 20)
```

Returns:

```text
30
```

### Tool 2 — `greet`

```python
greet("Anand")
```

Returns:

```text
Hello, Anand!
```

---

# 14. 🤖 Agent + MCP Concept

Eventually, the complete application can work like this:

```text
User
 │
 ▼
AI Agent
 │
 ▼
LLM — Gemma/Qwen
 │
 ▼
"Do I need a tool?"
 │
 ├── NO ───────────────► Answer
 │
 └── YES
       │
       ▼
    MCP Client
       │
       ▼
    MCP Server
       │
       ├── Calculator
       ├── File Tool
       ├── Search Tool
       └── Database Tool
              │
              ▼
           Result
              │
              ▼
          AI Agent
              │
              ▼
            User
```

This is the basic idea behind a **tool-using agent**.

The agent can:

1. Receive a user request.
2. Send the request to the LLM.
3. Determine whether a tool is required.
4. Call an MCP tool when necessary.
5. Receive the tool result.
6. Continue reasoning/workflow.
7. Return the final answer.

---

# 15. 📦 Check Everything

Run these commands one by one.

## 🐍 Python

```powershell
python --version
```

## 📦 pip

```powershell
pip --version
```

## 🦙 Ollama

```powershell
ollama --version
```

## 🧠 Installed Models

```powershell
ollama list
```

## 📦 All Python Packages

```powershell
pip list
```

## 🦜 LangChain

```powershell
pip show langchain
```

## 🦙 LangChain Ollama

```powershell
pip show langchain-ollama
```

## 🧠 LangGraph

```powershell
pip show langgraph
```

## ⚡ FastMCP

```powershell
pip show fastmcp
```

## 🔌 LangChain MCP Adapter

```powershell
pip show langchain-mcp-adapters
```

---

# 16. 🗂️ Recommended Final Project Structure

As the project grows, organize it like this:

```text
Agentic Ai/
│
├── venv/
│
├── agent/
│   ├── __init__.py
│   ├── agent.py
│   ├── graph.py
│   └── state.py
│
├── mcp/
│   ├── __init__.py
│   ├── server.py
│   └── tools.py
│
├── models/
│   └── ollama.py
│
├── tests/
│   └── test_agent.py
│
├── .env
├── .gitignore
├── requirements.txt
├── README.md
└── main.py
```

## 🔐 `.gitignore`

Do **not** commit the virtual environment or environment variables to GitHub.

Create a `.gitignore` file containing:

```gitignore
venv/
.env
__pycache__/
*.pyc
```

You can also add:

```gitignore
.pytest_cache/
.vscode/
.idea/
```

---

# 17. ⚡ Complete Setup Sequence

When starting the project from scratch:

```powershell
cd "X:\Agentic Ai"

python -m venv venv

Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned

.\venv\Scripts\Activate.ps1

python -m pip install --upgrade pip

pip install langchain langchain-ollama langgraph fastmcp langchain-mcp-adapters

pip freeze > requirements.txt

ollama --version

ollama list

ollama pull gemma4:12b

ollama run gemma4:12b
```

Ask the model something such as:

```text
What is Agentic AI?
```

Exit Ollama:

```text
/bye
```

Then run the Python test:

```powershell
python .\agent_mcp.py
```

---

# 🧩 The Most Important Mental Model

Do not memorize the packages as random commands.

Remember the architecture:

```text
                 AGENTIC AI APPLICATION
                          │
                          ▼
                     LangGraph
                  Agent Workflow
                          │
                          ▼
                     LangChain
                 LLM + Tool Logic
                    │          │
                    ▼          ▼
                 Ollama       MCP
                    │          │
                    ▼          ▼
              Gemma/Qwen   MCP Server
                              │
                         ┌────┼────┐
                         ▼    ▼    ▼
                       Tools Tools Tools
```

## 🧠 One-Sentence Summary

> **Ollama runs the LLM, LangChain connects your application to the LLM and tools, LangGraph manages the agent workflow, MCP provides a standard way to expose and use tools, and FastMCP makes building MCP servers easier.**

---

# 🎯 Final Architecture

The complete learning path is:

```text
                    USER
                      │
                      ▼
                AGENTIC AI APP
                      │
                      ▼
                  LangGraph
                Agent Workflow
                      │
                      ▼
                  LangChain
                 /         \
                /           \
               ▼             ▼
           Ollama            MCP
              │                │
              ▼                ▼
        Gemma / Qwen       MCP Client
                               │
                               ▼
                          MCP Server
                               │
                  ┌────────────┼────────────┐
                  ▼            ▼            ▼
             Calculator    File Tool    Database
                  │            │            │
                  └────────────┼────────────┘
                               ▼
                            Result
                               │
                               ▼
                             Agent
                               │
                               ▼
                            User
```

## 🚀 Learning Progression

```text
Python
  ↓
Virtual Environment
  ↓
Ollama
  ↓
Local LLM
  ↓
LangChain
  ↓
LangGraph
  ↓
MCP
  ↓
FastMCP
  ↓
MCP Tools
  ↓
Tool-Using Agent
  ↓
Agentic AI Application
```

---

## ✅ Setup Checklist

* [ ] Python installed
* [ ] Project directory created
* [ ] Virtual environment created
* [ ] Virtual environment activated
* [ ] pip upgraded
* [ ] LangChain installed
* [ ] LangChain Ollama installed
* [ ] LangGraph installed
* [ ] FastMCP installed
* [ ] LangChain MCP Adapters installed
* [ ] Ollama installed
* [ ] Ollama verified
* [ ] LLM downloaded
* [ ] Ollama tested
* [ ] LangChain + Ollama tested
* [ ] LangGraph tested
* [ ] MCP server created
* [ ] `.gitignore` created
* [ ] `requirements.txt` generated

---

## 🎉 Conclusion

You now have the foundation for a local **Agentic AI + MCP** development environment.

The core technologies have different responsibilities:

```text
Python
  → Programming Language

Ollama
  → Runs Local LLM

Gemma / Qwen
  → Language Model

LangChain
  → LLM + Tool Integration

LangGraph
  → Agent Workflow + State

MCP
  → Standard Tool/Data Protocol

FastMCP
  → MCP Server Development

MCP Server
  → Provides Tools

Agent
  → Decides When and How to Use Tools
```

The ultimate goal is to build an agent that can:

```text
Understand
    ↓
Reason
    ↓
Plan
    ↓
Choose Tools
    ↓
Execute Tools
    ↓
Observe Results
    ↓
Continue
    ↓
Answer
```

**This is the foundation for building modern tool-using and Agentic AI applications with local LLMs.**
