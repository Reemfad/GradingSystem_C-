from state import GradingState, GradingResult
from debug_log import agent_start, agent_done, token_estimate, tpm_status, rpm_wait

def optimizer_refinement_agent(state: GradingState) -> GradingState:
    agent_start("optimizer", "🟢")
    # print(f"🔁 Optimizer iteration {i+1}/{MAX_OPTIMIZER_LOOPS}")
    evaluation = state.partial_results["evaluation"]
    meta = state.partial_results["meta_evaluation"]

    # Stop if evaluator is confident
    if meta.confidence == "high":
        state.final_result = state.final_result
        return state

    updated_breakdown = {}

    for item in evaluation.breakdown:
        score = item.score

        for adj in meta.suggested_adjustments:
            if adj.criterion == item.criterion:
                score += adj.delta

        updated_breakdown[item.criterion] = f"{score} points"

    new_total = sum(
        int(v.split()[0]) for v in updated_breakdown.values()
    )

    state.final_result = GradingResult(
        final_score=new_total,
        breakdown=updated_breakdown,
        explanation=(
            state.final_result.explanation +
            " Grade refined after evaluator feedback."
        )
    )
    
    return state
