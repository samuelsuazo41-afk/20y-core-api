from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

app = FastAPI(
    title="20Y Core API + Coach Atlas",
    description="1 Número + 1 Acción = Imperio. Bajo Licencia 20Y",
    version="2.0.0"
)

class AtlasInput(BaseModel):
    hrv: Optional[float] = 40
    recovery: Optional[float] = 50
    deal_stage: Optional[str] = "none"
    user_level: Optional[int] = 1
    license_key: Optional[str] = "20Y-MOD-2026"

@app.get("/")
def root():
    return {
        "status": "20Y Core API Online",
        "atlas_module": "Coach Atlas v2.0 Active",
        "version": "2.0.0",
        "legal": "Operando bajo 20Y Modification License",
        "copyright": f"© {datetime.now().year} Samuel Suazo"
    }

@app.post("/atlas")
def coach_atlas(data: AtlasInput):
    score = (data.hrv * 0.4 + data.recovery * 0.6)
    level_bonus = data.user_level * 5
    final_score = min(score + level_bonus, 100)

    if data.user_level >= 9:
        accion = "NIVEL 9: Llama a Rahul 10:00h. Cierra deal 48h o muere."
        nivel = "Dios del Deal"
        prioridad = "CRITICA"
    elif data.user_level >= 5:
        accion = "NIVEL 5+: Deep Work 6h. Eres estratega."
        nivel = "Arquitecto"
        prioridad = "ALTA"
    else:
        accion = "NIVEL 1-4: Shipea hoy 18:00h."
        nivel = "Constructor"
        prioridad = "MEDIA"

    return {
        "score_360": round(final_score, 1),
        "nivel_usuario": data.user_level,
        "nivel_nombre": nivel,
        "accion": accion,
        "prioridad": prioridad,
        "deadline": "48h",
        "powered_by": "20Y Core"
    }