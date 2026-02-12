from langchain_openai import ChatOpenAI
from config import MODEL_NAME, TEMPERATURE
from prompts import EDGE_CASE_PROMPT
from state import GradingState, PartialResult
import json

llm = ChatOpenAI(model=MODEL_NAME, temperature=TEMPERATURE)

def edge_agent(state: GradingState) -> GradingState:
    response = llm.invoke(
        EDGE_CASE_PROMPT + f"\nStudent Code:\n{state.input.student_code}"
    )
    data = json.loads(response.content)

    state.partial_results["edge_cases"] = PartialResult(**data)
    return state
