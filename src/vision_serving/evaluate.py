from .metrics import validate_response
from .model import ModelRouter


def evaluate(config_path="config/default.yaml"):
    router = ModelRouter({"classification": lambda x: {"class_id": 0, "score": 0.99}})
    out = router.predict("classification", [0.1, 0.2])
    return {"contract_valid": validate_response(out)}
