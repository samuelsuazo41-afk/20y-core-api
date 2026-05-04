from pydantic import BaseModel
from cerebro_20y import Cerebro20Y
import uvicorn

app = FastAPI(title="20Y Core API", version="3.0-EDGE")
cerebro = Cerebro20Y()

class WearablesInput(BaseModel):
    hrv: float = 50
    rhr: float = 55
    sleep_h: float = 7.0
    steps: int = 8000
    stress: int = 30

@app.get("/")
def root():
    return {"status": "20Y Core Online", "mae": cerebro.mae, "version": cerebro.version}

@app.post("/score")
def get_score(data: WearablesInput):
    result = cerebro.score_360(data.dict())
    return result

@app.get("/health")
def health():
    return {"status": "healthy", "p95_target_ms": 50}
    @app.get("/atlas/pulso")
async def atlas_pulso():
    return {
        "stability_20y": 1,
        "version": "8.0.0",
        "p95_ms": 42  # Cambia 42 por tu p95 real si lo mides
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
