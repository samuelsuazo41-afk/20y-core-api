from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

app = FastAPI(
    title="Coach Atlas - Powered by 20Y License",
    description="Módulo independiente bajo licencia de modificación 20Y",
    version="2.0.0"
)

class AtlasInput(BaseModel):
    hrv: Optional[float] = 40
    recovery: Optional[float] = 50
    deal_stage: Optional[str] = "none"
    user_level: Optional[int] = 1
    license_key: Optional[str] = None

@app.get("/")
def root():
    return {
        "status": "Coach Atlas Online",
        "version": "2.0.0",
        "legal": "Operando bajo 20Y Modification License",
        "copyright": f"© {datetime.now().year} Samuel Suazo. Atlas Module."
    }

@app.post("/atlas")
def coach_atlas(data: AtlasInput):
    if not data.license_key:
        return {"error": "License key requerida", "status": 401}

    score = (data.hrv * 0.4 + data.recovery * 0.6)
    level_bonus = data.user_level * 5
    final_score = min(score + level_bonus, 100)

    if data.user_level >= 9:
        accion = "NIVEL 9: Acceso Billonario. Llama a Rahul 10:00h. Cierra deal o muere."
        prioridad = "CRITICA"
        nivel_nombre = "Dios del Deal"
    elif data.user_level >= 5:
        accion = "NIVEL 5+: Deep Work 6h. Ya no eres operador, eres estratega."
        prioridad = "ALTA"
        nivel_nombre = "Arquitecto"
    elif final_score < 70:
        accion = "NIVEL 1-4: Shipea hoy 18:00h. Construye margen de seguridad."
        prioridad = "MEDIA"
        nivel_nombre = "Constructor"
    else:
        accion = "Ejecuta long-term. Nivel insuficiente para deals críticos."
        prioridad = "BAJA"
        nivel_nombre = "Aprendiz"

    return {
        "score_360": round(final_score, 1),
        "nivel_usuario": data.user_level,
        "nivel_nombre": nivel_nombre,
        "accion": accion,
        "prioridad": prioridad,
        "deadline": "48h",
        "license_valid": True
  }
