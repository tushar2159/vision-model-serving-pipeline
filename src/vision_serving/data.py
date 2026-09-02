from pydantic import BaseModel
class InferenceRequest(BaseModel):
    task: str
    values: list[float]
