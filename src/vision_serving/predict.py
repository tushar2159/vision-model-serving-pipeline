from .model import ModelRouter


def build_demo_router():
    return ModelRouter(
        {
            "classification": lambda x: {"class_id": int(sum(x) > 0), "score": 0.9},
            "segmentation": lambda x: {"mask_shape": [64, 64]},
            "detection": lambda x: {"detections": []},
        }
    )
