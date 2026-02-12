from grader import grade
from state import GradingInput

input_data = GradingInput(
    problem="Write a function that returns the factorial of a number.",
    reference_solution="""
int fact(int n){
    if(n <= 1) return 1;
    return n * fact(n-1);
}
""",
    rubric="""
- Correct output for typical inputs (1–10): 35 points
- Handling of fact(0) returning 1: 15 points
- Behavior for negative inputs (reject, document, or guard): 15 points
- Function completeness (correct return type and always returns a value): 15 points
- Valid factorial algorithm (iterative or recursive): 10 points
- Awareness or handling of integer overflow / large n: 10 points
""",
    student_code="""
int fact(int n){
    int res = 1;
    for(int i=1;i<=n;i++)
        res *= i;
    
}
"""
)

result = grade(input_data)

print("Final Score:", result.final_score)
print("Breakdown:", result.breakdown)
print("Explanation:", result.explanation)
