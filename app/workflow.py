from langgraph.graph import StateGraph
from state import GradingState
from analysis_agent import analysis_agent
from evaluator_agent import evaluator_agent
from meta_evaluator_agent import meta_evaluator_agent
from optimizer_refinement_agent import optimizer_refinement_agent



def build_workflow():
    graph = StateGraph(GradingState)

    graph.add_node("analysis", analysis_agent)
    graph.add_node("evaluation", evaluator_agent)
    graph.add_node("meta_evaluation", meta_evaluator_agent)
    graph.add_node("refinement", optimizer_refinement_agent)


    graph.set_entry_point("analysis")
    graph.add_edge("analysis", "evaluation")
    graph.add_edge("evaluation", "meta_evaluation")
    graph.add_edge("meta_evaluation", "refinement")
    graph.set_finish_point("refinement")



    # graph.set_finish_point("evaluation")

    return graph.compile()
