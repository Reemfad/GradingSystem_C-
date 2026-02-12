from fastapi import FastAPI
from grader import grade
from state import GradingInput

app = FastAPI()

@app.post("/grade")
def grade_endpoint(input_data: GradingInput):
    return grade(input_data)
