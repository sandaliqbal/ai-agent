import uuid
from langchain.messages import HumanMessage
from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.prebuilt import ToolNode

from agent_state import AgentState
from tools import check_weather

# Initialize LLM (Ollama local model)
llm = ChatOllama(model="gpt-oss:20b", temperature=0)

# Bind available tools
tools = [check_weather]
llm_with_tools = llm.bind_tools(tools)


def agent_node(state: AgentState):
    """
    Main agent node.
    Takes the conversation state, sends messages to LLM, and returns output.
    """
    messages = state["messages"]
    response = llm_with_tools.invoke(messages)  # LLM generates next message
    return {"messages": [response]}


# Tool execution node (LangGraph built-in)
tool_node = ToolNode(tools)


def should_continue(state: AgentState):
    """
    Routing function.
    If the LLM returns a tool call, we route to the tools node.
    Otherwise, end the graph execution.
    """
    last_message = state["messages"][-1]
    if last_message.tool_calls:
        return "continue_to_tools"
    return "end"


# Build the workflow graph
workflow = StateGraph(AgentState)

workflow.add_node("agent", agent_node)
workflow.add_node("tools", tool_node)

workflow.set_entry_point("agent")
workflow.add_edge(START, "agent")

workflow.add_conditional_edges(
    "agent",
    should_continue,
    {
        "continue_to_tools": "tools",
        "end": END,
    },
)

workflow.add_edge("tools", END)

# Compile graph with in-memory checkpointing (stores per-thread conversation)
graph = workflow.compile(checkpointer=InMemorySaver())


def agent_reply(user_message: str, thread_id: str):
    """
    Streams responses from the agent.
    Each browser window should get its own thread_id.
    """
    config = {"configurable": {"thread_id": thread_id}}
    inputs = {"messages": [HumanMessage(content=user_message)]}
    return graph.stream(inputs, config)
