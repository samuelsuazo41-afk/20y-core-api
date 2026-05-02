import math
import json
from datetime import datetime, timedelta

class Cerebro20Y:
    def __init__(self):
        self.version = "3.0-EDGE"
        self.mae = 11.8
        
    def score_360(self, wearables):
        hrv = wearables.get('hrv', 50)
        rhr = wearables.get('rhr', 55) 
        sleep_h = wearables.get('sleep_h', 7.0)
        steps = wearables.get('steps', 8000)
        stress = wearables.get('stress', 30)
        
        recovery = (hrv * 0.4) + ((100 - rhr) * 0.3) + (sleep_h * 8 * 0.3)
        capacity = (steps / 10000 * 100) * 0.5 + ((100 - stress) * 0.5)
        energy_score = (recovery * 0.6 + capacity * 0.4)
        
        if energy_score > 85: ttp = 3; speech = "Nivel Elite. Ve a por el reto mas duro hoy."
        elif energy_score > 70: ttp = 7; speech = "Nivel Optimo. 70% foco en tu tarea clave."
        elif energy_score > 50: ttp = 14; speech = "Nivel Carga. 1 sola tarea. Repara sueno hoy."
        else: ttp = 21; speech = "Nivel Recarga. Solo recuperar. Sin decisiones."
            
        return {
            "score_360": round(energy_score, 1),
            "ttp_days": ttp,
            "speech": speech,
            "mae": self.mae,
            "timestamp": datetime.now().isoformat()
      }
