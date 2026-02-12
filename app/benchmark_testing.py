import json
from grader import grade
from state import GradingInput
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import numpy as np



with open("app/Dataset.json", "r") as data:
    dataset = json.load(data)

results = []

for question in dataset["questions"]:
    problem = question["description"]
    reference_solution = question["reference_solution"]
    
    # Combine rubric points into a string format for your grader
    rubric_str = ""
    for r in question["rubric"]:
        rubric_str += f"- {r['criterion']}: {r['points']} points\n"
    
    for submission in question["student_submissions"]:
        student_code = submission["code"]
        human_score = submission["human_score"]
        
        input_data = GradingInput(
            problem=problem,
            reference_solution=reference_solution,
            rubric=rubric_str,
            student_code=student_code
        )
        
        result = grade(input_data)
        
        results.append({
            "question_id": question["id"],
            "student_code": student_code,
            "human_score": human_score,
            "llm_score": result.final_score,
            "workflow": "evaluator_optimizer",
            "breakdown": result.breakdown,
            "explanation": result.explanation
        })

        print({
                "question_id": question["id"],
                "human_score": human_score,
                "llm_score": result.final_score
            })


human_points = np.array([r["human_score"] for r in results])
llm_points   = np.array([r["llm_score"] for r in results])

mae = np.mean(np.abs(human_points - llm_points))
print("Mean Absolute Error (MAE):", mae)


