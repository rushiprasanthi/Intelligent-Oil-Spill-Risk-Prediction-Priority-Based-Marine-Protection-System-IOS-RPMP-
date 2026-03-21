from pydantic import BaseModel
from typing import Dict, List


class RiskExplanation(BaseModel):
    summary: str
    factors: List[str]


class RiskResponse(BaseModel):
    exposure: float
    risk_score: float
    priority: str
    priority_label: str
    explanation: RiskExplanation
