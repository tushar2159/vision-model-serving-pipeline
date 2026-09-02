from dataclasses import dataclass
from typing import Any

@dataclass
class ModelRouter:
    handlers: dict[str, Any]
    def predict(self, task: str, payload: Any) -> dict:
        if task not in self.handlers:
            raise ValueError(f"unsupported task: {task}")
        return {"task": task, "result": self.handlers[task](payload)}
