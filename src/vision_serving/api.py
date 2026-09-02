from fastapi import FastAPI

from .data import InferenceRequest
from .predict import build_demo_router

app = FastAPI(
    title="Vision Model Serving Pipeline",
    version="0.1.0",
    description="Validated task routing for public-safe demonstration models.",
)
router = build_demo_router()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/ready")
def ready():
    return {"status": "ready", "tasks": sorted(router.handlers)}


@app.get("/metadata")
def metadata():
    return {"service": app.title, "version": app.version, "model_mode": "demo"}


@app.post("/predict")
def predict(req: InferenceRequest):
    return router.predict(req.task, req.values)
