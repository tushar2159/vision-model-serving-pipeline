from typing import Literal

from pydantic import BaseModel, Field


class InferenceRequest(BaseModel):
    task: Literal["classification", "segmentation", "detection"]
    values: list[float] = Field(min_length=1, max_length=4096)
