from pydantic import BaseModel, Field
from typing import Dict, Optional, List
from typing import List

class GradingInput(BaseModel):
    problem: str
    reference_solution: str
    rubric: str
    student_code: str


class AnalysisResult(BaseModel):
    correct_components: List[str]
    missing_components: List[str]
    logical_errors: List[str]
    quality_issues: List[str]





class GradingResult(BaseModel):
    final_score: int
    breakdown: Dict[str, str]
    explanation: str


class GradingState(BaseModel):
    input: GradingInput
    partial_results: Dict[str, BaseModel] = {}
    final_result: Optional[GradingResult] = None

class BreakdownItem(BaseModel):    
    """Individual criterion score breakdown"""    
    criterion: str    
    score: int = Field(ge=0)

class EvaluationResult(BaseModel):    
    final_score: int = Field(ge=0, le=100)    
    breakdown: List[BreakdownItem]  # ✅ Now matches prompt structure    explanation: str
    explanation: str



class Adjustment(BaseModel):
    criterion: str
    delta: int  # positive or negative score adjustment


class MetaEvaluationResult(BaseModel):
    issues: List[str]
    suggested_adjustments: List[Adjustment]
    confidence: str  # "low", "medium", "high"
