from langchain_openai import ChatOpenAI
from state import GradingState, MetaEvaluationResult
from prompts import META_EVALUATOR_PROMPT
from config import MODEL_NAME, TEMPERATURE
from debug_log import agent_start, agent_done, token_estimate, tpm_status, rpm_wait
llm = ChatOpenAI(
    model=MODEL_NAME,
    temperature=TEMPERATURE
)

meta_llm = llm.with_structured_output(
    MetaEvaluationResult,
    method="function_calling"
)

def meta_evaluator_agent(state: GradingState) -> GradingState:
    agent_start("meta-evaluator", "🟣")
    grading = state.partial_results["evaluation"]
    analysis = state.partial_results["analysis"]

    prompt = f"""
{META_EVALUATOR_PROMPT}

Rubric:
{state.input.rubric}

Analysis:
{analysis}

Initial Grading:
{grading}
"""

    meta_result = meta_llm.invoke(prompt)
    state.partial_results["meta_evaluation"] = meta_result
    agent_done("meta-evaluator", f"(confidence={meta_result})")
    return state
