from src.Coder_Buddy.nodes.orchastrator_node import orchastrator
from langgraph.graph import StateGraph,START,END
from src.Coder_Buddy.nodes.filesCreator_node import create_files
from src.Coder_Buddy.models.Orchastrator_model import State
import logging


graph=StateGraph(state_schema=State)

graph.add_node("file_creator",create_files)


graph.add_edge(START,"file_creator")
graph.add_edge("file_creator", END)


graph=graph.compile()

with open("FileWriterWorkflow.png","wb") as f:
    f.write(graph.get_graph().draw_mermaid_png())

