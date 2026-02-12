from langchain_openai import ChatOpenAI
from state import GradingState, EvaluationResult, GradingResult
from prompts import EVALUATOR_PROMPT_COT
from config import MODEL_NAME, TEMPERATURE
from debug_log import agent_start, agent_done, token_estimate, tpm_status, rpm_wait
# from llm_gate import llm_gate
# from config import MAX_TOKENS_EVALUATOR


llm = ChatOpenAI(
    model=MODEL_NAME,
    temperature=TEMPERATURE
)

# evaluator_llm = llm.with_structured_output(EvaluationResult)
evaluator_llm = llm.with_structured_output(
    EvaluationResult,
    method="function_calling"
)

def evaluator_agent(state: GradingState) -> GradingState:
    agent_start("evaluator", "🟠")
    analysis = state.partial_results["analysis"]

    prompt = f"""
{EVALUATOR_PROMPT_COT}

Rubric:
{state.input.rubric}

Analysis Findings:
Correct Components:
{analysis.correct_components}

Missing Components:
{analysis.missing_components}

Logical Errors:
{analysis.logical_errors}

Quality Issues:
{analysis.quality_issues}
"""

    evaluation: EvaluationResult = evaluator_llm.invoke(prompt)

    state.partial_results["evaluation"] = evaluation

    state.final_result = GradingResult(
    final_score=evaluation.final_score,
    breakdown={item.criterion: f"{item.score} points" for item in evaluation.breakdown},
    explanation=evaluation.explanation
)

    
    
   

    return state
    
