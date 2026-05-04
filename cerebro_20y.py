from datetime import datetime

class Cerebro20Y:
    """ 
    Regla única: stability_20y >= 7
    Si falla 1 regla = Día 0
    """
    def __init__(self):
        self.version = "8.0.0"
        self.dia_actual = 1
    
    def check_6am(self, rituales: list) -> bool:
        return len(rituales) >= 3
    
    def check_12pm(self, score_calor: int) -> bool:
        return score_calor >= 7
    
    def check_22pm(self, post_hecho: bool, reporte: bool) -> bool:
        return post_hecho and reporte
    
    def calcular_stability(self, checks: dict) -> int:
        if not all(checks.values()):
            self.dia_actual = 0 # RESET
            return 0
        # Lógica MAE 11.8 aquí
        return min(10, self.dia_actual)
    
    def reset_si_falla(self):
        self.dia_actual = 0
        return "Día 0. Vuelves a empezar."
