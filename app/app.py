import streamlit as st
from grader import grade
from state import GradingInput

st.set_page_config(
    page_title="LLM Code Grading System",
    page_icon="⚡",
    layout="wide"
)

# Header
st.title("⚡ LLM Code Grading System")
st.markdown("**Chain-of-Thought Analysis with Evaluator-Optimizer Workflow**")
st.info("**Workflow:** Analysis Agent → Evaluator Agent → Meta-Evaluator Agent → Optimizer Refinement")

# Load example button
if st.button("Load Example"):
    st.session_state['problem'] = "Write a function that returns the factorial of a number."
    st.session_state['reference'] = """int fact(int n){
                                            if(n <= 1) return 1;
                                            return n * fact(n-1);
                                        }"""
    st.session_state['rubric'] = """- Correct output for typical inputs (1–10): 35 points
- Handling of fact(0) returning 1: 15 points
- Behavior for negative inputs (reject, document, or guard): 15 points
- Function completeness (correct return type and always returns a value): 15 points
- Valid factorial algorithm (iterative or recursive): 10 points
- Awareness or handling of integer overflow / large n: 10 points"""
    
    st.session_state['student'] = """int fact(int n){
                                        int res = 1;
                                        for(int i=1;i<=n;i++)
                                            res *= i;
                                        
                                    }"""

# Input fields
col1, col2 = st.columns(2)

with col1:
    problem = st.text_area(
        "📖 Problem Description",
        value=st.session_state.get('problem', ''),
        height=150
    )
    
    rubric = st.text_area(
        "📄 Grading Rubric",
        value=st.session_state.get('rubric', ''),
        height=150
    )

with col2:
    reference_solution = st.text_area(
        "✅ Reference Solution",
        value=st.session_state.get('reference', ''),
        height=150
    )
    
    student_code = st.text_area(
        "🔶 Student Code",
        value=st.session_state.get('student', ''),
        height=150
    )

# Grade button
if st.button("Grade Submission", type="primary"):
    if problem and reference_solution and rubric and student_code:
        with st.spinner("Grading in progress..."):
            input_data = GradingInput(
                problem=problem,
                reference_solution=reference_solution,
                rubric=rubric,
                student_code=student_code
            )
            result = grade(input_data)
            
            # Display results
            score_color = "green" if result.final_score >= 90 else "blue" if result.final_score >= 70 else "orange" if result.final_score >= 50 else "red"
            
            st.markdown(f"## Final Score: :{score_color}[{result.final_score}/100]")
            
            st.subheader("Score Breakdown")
            for criterion, points in result.breakdown.items():
                st.write(f"- **{criterion}**: {points}")
            
            st.subheader("Explanation")
            st.info(result.explanation)
    else:
        st.error("Please fill in all fields")