from datetime import datetime

class Registro:
    def __init__(self, vehiculo):
        self.vehiculo = vehiculo
        self.hora_ingreso = datetime.now()
        self.hora_salida = None

    def registrar_salida(self):
        self.hora_salida = datetime.now()

    def calcular_horas(self):
        if self.hora_salida:
            tiempo = self.hora_salida - self.hora_ingreso
            return tiempo.total_seconds() / 3600
        return 0