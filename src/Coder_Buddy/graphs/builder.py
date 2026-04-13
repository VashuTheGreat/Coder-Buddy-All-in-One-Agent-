from langgraph.graph import StateGraph, START, END
import sys
import os
from dotenv import load_dotenv
load_dotenv()
sys.path.append(os.getcwd())
from src.Coder_Buddy.graphs.orchastrator.orchastrator_graph import graph as orchastrator_subgraph
from src.Coder_Buddy.graphs.fileWriter.fileWriter_graph import graph as create_files_subgraph
from src.Coder_Buddy.nodes.coder_node import coder_node
from src.Coder_Buddy.nodes.malfunctionDetector_node import malfunction_handler_node
from src.Coder_Buddy.models.Orchastrator_model import State
import logging
from exception import MyException

graph=StateGraph(State)

graph.add_node("orchastrator",orchastrator_subgraph)
graph.add_node("file_writer",create_files_subgraph)
graph.add_node("coder",coder_node)
graph.add_node("malfunction_handler",malfunction_handler_node)


# ================== Defining edges for normal workflow ==================
graph.add_edge(START,"orchastrator")
graph.add_edge("orchastrator","file_writer")
graph.add_edge("file_writer","coder")
graph.add_edge("coder", "malfunction_handler")
graph.add_conditional_edges(
    "malfunction_handler",
    lambda state: "coder" if state.malfunction_detected else "end",
    {"coder": "coder", "end": END}
)


graph=graph.compile()


try:    
    with open("graph.png", "wb") as f:
        f.write(graph.get_graph().draw_mermaid_png())
    logging.info("Graph visualization saved to file_writer_graph.png")
except Exception as e:
    logging.warning(f"Could not save graph PNG (non-fatal): {e}")
    raise MyException(f"Graph visualization failed: {e}")
