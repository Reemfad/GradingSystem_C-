from state import GradingInput, GradingState, AnalysisResult
from analysis_agent import analysis_agent


def test_analysis_agent_produces_analysis_result():
    input_data = GradingInput(
        problem="Check if a number is prime",
        reference_solution="bool isPrime(int n) { /* correct logic */ }",
        rubric="Logic: 100",
        student_code="bool isPrime(int n){ return n > 1; }"
    )

    state = GradingState(input=input_data)

    new_state = analysis_agent(state)

    # ---- PRINT OUTPUT ----
    # print("\n=== Analysis Agent Output ===")
    # analysis = new_state.partial_results.get("analysis")
    # print(analysis.json(indent=2))

    # ✅ Analysis agent should NOT produce final result
    assert new_state.final_result is None

    # ✅ Analysis result must exist
    assert "analysis" in new_state.partial_results

    analysis = new_state.partial_results["analysis"]
    assert isinstance(analysis, AnalysisResult)

    # ✅ Required fields must exist
    assert isinstance(analysis.correct_components, list)
    assert isinstance(analysis.missing_components, list)
    assert isinstance(analysis.logical_errors, list)
    assert isinstance(analysis.quality_issues, list)


test_analysis_agent_produces_analysis_result()