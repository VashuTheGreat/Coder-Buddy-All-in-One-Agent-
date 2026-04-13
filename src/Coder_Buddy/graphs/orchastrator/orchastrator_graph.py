from src.Coder_Buddy.nodes.orchastrator_node import orchastrator
from langgraph.graph import StateGraph,START,END
from langgraph.types import Send
from src.Coder_Buddy.models.Orchastrator_model import State
from src.Coder_Buddy.nodes.worker_node import worker
from src.Coder_Buddy.nodes.reduce_worker_outputs_node import reduce_worker_outputs
import logging



def fan_out_tasks(state: State):
    return [
        Send("worker", {"current_task": task, "plan": state.plan})
        for task in state.tasks
    ]

graph=StateGraph(state_schema=State)

graph.add_node("orchastrator",orchastrator)
graph.add_node("worker",worker)
graph.add_node("reduce_worker_outputs",reduce_worker_outputs)


graph.add_edge(START,"orchastrator")
graph.add_conditional_edges("orchastrator",fan_out_tasks,["worker"])
graph.add_edge("worker","reduce_worker_outputs")
graph.add_edge("reduce_worker_outputs", END)

graph=graph.compile()


with open("Workflow.png","wb") as f:
    f.write(graph.get_graph().draw_mermaid_png())