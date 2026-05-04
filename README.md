# 20Y app - Edge-First OS for Human Energy

**Regla única**: `stability_20y >= 7` o reset a Día 0. Sin excusas.

## Qué es
OS que mide disciplina diaria. MAE 11.8, p95 <50ms. 1 número. 1 acción. 1 post.

## Día 1 Live
- **API**: `https://20y-core-api.onrender.com/atlas/pulso`
- **Stack**: Python 3.11, FastAPI, Render
- **Racha**: Día 1 inicia hoy

## Reglas 20Y
1. **6am**: 3 rituales o Día 0
2. **12pm**: Score calor o Día 0 
3. **22pm**: Post + reporte o Día 0

## Endpoints
`GET /atlas/pulso` → `{"stability_20y": 1-10, "version": "8.0.0", "p95_ms": <50}`

## Deploy
```bash
pip install -r requirements.txt
uvicorn api_20y:app --host 0.0.0.0 --port 10000
