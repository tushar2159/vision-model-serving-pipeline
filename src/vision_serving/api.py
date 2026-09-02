from fastapi import FastAPI, HTTPException
from .data import InferenceRequest
from .predict import build_demo_router

app=FastAPI(title="Vision Model Serving Pipeline",version="0.1.0")
router=build_demo_router()

@app.get("/health")
def health():
    return {"status":"ok"}

@app.post("/predict")
def predict(req: InferenceRequest):
    try:
        return router.predict(req.task,req.values)
    except ValueError as e:
        raise HTTPException(status_code=400,detail=str(e))
