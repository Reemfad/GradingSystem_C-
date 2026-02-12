from workflow import build_workflow
from state import GradingInput, GradingState,GradingResult


workflow = build_workflow()




def grade(input_data: GradingInput) -> GradingResult:
    state = GradingState(input=input_data)
    final_state = workflow.invoke(state)
    return final_state["final_result"]
