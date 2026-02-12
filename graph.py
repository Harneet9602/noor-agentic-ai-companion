import sqlite3
from langgraph.graph import StateGraph, END
from langgraph.checkpoint.sqlite import SqliteSaver
from state import AgentState
from nodes import supervisor_node, therapist_node, habit_node, safety_node

#Initialize the Graph
workflow = StateGraph(AgentState)

#Add the nodes (The Agents)
workflow.add_node("supervisor", supervisor_node)
workflow.add_node("therapist",therapist_node)
workflow.add_node("safety", safety_node)
workflow.add_node("habit", habit_node)

#Define the Entry point
#The conversation always starts with the Supervisor analyzing the input.
workflow.set_entry_point("supervisor")

#Add Conditional Edges (Routing Logic)
#The Supervisor returns a 'next' key (either 'THERAPIST' or 'SAFETY').
#We map that return value to the actual node names we defined in step 2.
workflow.add_conditional_edges(
    'supervisor',
    lambda state: state['next'],
    {
       'THERAPIST': 'therapist',
       'SAFETY': 'safety',
       'HABIT': 'habit'
    }
)

# Add Normal Edges (Looping or Ending)
# After the therapist or safety agent speaks, we end this turn.
workflow.add_edge("therapist",END)
workflow.add_edge('safety',END)
workflow.add_edge('habit',END)

conn = sqlite3.connect("memory.sqlite", check_same_thread=False)
memory = SqliteSaver(conn)

#Compile the graph with memory
app = workflow.compile(checkpointer=memory)

# from graph import app

# # This generates the Mermaid syntax for your graph
# print(app.get_graph().draw_mermaid())
# try:
#     png_data = app.get_graph().draw_mermaid_png()
#     with open("mental_health_bot_structure.png", "wb") as f:
#         f.write(png_data)
#     print("Graph saved as 'mental_health_bot_structure.png'!")
# except Exception:
#     print("To save as PNG, you need to install graphviz.")
#     print("For now, copy the text output above and paste it into https://mermaid.live")