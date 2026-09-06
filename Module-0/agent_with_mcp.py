# agent.py
import asyncio
from langchain_openai import ChatOpenAI
from langchain.mcp import MCPAdapter
from langgraph.prebuilt import create_react_agent

async def main():
    # Initialize the OpenAI model (Ensure OPENAI_API_KEY is in your environment variables)
    model = ChatOpenAI(model="gpt-4o", temperature=0)

    # Open a connection to our local math server file via stdio transport
    # The adapter handles launching and talking to the background subprocess
    async with MCPAdapter(
        command="python",
        args=["math_server.py"],
        transport="stdio"
    ) as adapter:
        
        # Discover and format the server's tools dynamically
        tools = await adapter.list_tools()
        
        # Build a standard React Agent using the fetched tools
        agent = create_react_agent(model, tools)
        
        # Invoke the agent with a prompt requiring mathematical calculation
        query = {"messages": [{"role": "user", "content": "What is 15 multiplied by 10, then add 5 to it?"}]}
        response = await agent.ainvoke(query)
        
        # Print out the final answer from the agent
        print(response["messages"][-1].content)

if __name__ == "__main__":
    asyncio.run(main())
