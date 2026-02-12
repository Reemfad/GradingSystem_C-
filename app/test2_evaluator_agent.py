from state import GradingInput, GradingState, AnalysisResult
from evaluator_agent import evaluator_agent


def test_evaluator_agent_produces_final_result():
    input_data = GradingInput(
        problem="Check if a number is prime",
        reference_solution="bool isPrime(int n) { /* correct logic */ }",
        rubric=""""
        - Correct recursion logic: 60 points
        - Base case handling: 20 points
        - Code quality and readability: 20 points""",
        student_code="bool isPrime(int n){ return n > 1; }"
    )

    state = GradingState(input=input_data)

    # 👇 Manually inject analysis result (unit test isolation)
    state.partial_results["analysis"] = AnalysisResult(
        correct_components=["Correct function signature"],
        missing_components=["Does not check divisibility"],
        logical_errors=["Returns true for non-prime numbers"],
        quality_issues=["there are no quality issues"]
    )

    new_state = evaluator_agent(state)

    # ✅ Final grading must exist
    assert new_state.final_result is not None

    result = new_state.final_result

    assert 0 <= result.final_score <= 100
    assert isinstance(result.breakdown, dict)
    # assert len(result.breakdown) > 0
    assert isinstance(result.explanation, str)
test_evaluator_agent_produces_final_result()