from fastapi import APIRouter
from backend.schemas.spill_schema import SpillRequest
from backend.controllers.spill_controller import handle_spill

router = APIRouter()

@router.post("/simulate_spill")
def simulate_spill(spill: SpillRequest):
    return handle_spill(spill)
