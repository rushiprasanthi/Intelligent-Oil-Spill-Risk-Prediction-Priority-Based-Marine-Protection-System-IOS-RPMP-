from pydantic import BaseModel

class SpillRequest(BaseModel):
    lat: float
    lng: float
    spill_size: float
