from langchain_openai import ChatOpenAI
from state import GradingState, AnalysisResult
from prompts import ANALYSIS_PROMPT_COT
from config import MODEL_NAME, TEMPERATURE

from debug_log import agent_start, agent_done, token_estimate, tpm_status

llm = ChatOpenAI(
    model=MODEL_NAME,
    temperature=TEMPERATURE
)

analysis_llm = llm.with_structured_output(AnalysisResult)

def analysis_agent(state: GradingState) -> GradingState:
    agent_start("analysis", "🔵")
    prompt = f"""
{ANALYSIS_PROMPT_COT}

Problem:
{state.input.problem}

Reference Solution:
{state.input.reference_solution}

Student Code:
{state.input.student_code}
"""

    analysis_result: AnalysisResult = analysis_llm.invoke(prompt)
    state.partial_results["analysis"] = analysis_result
    return state
    