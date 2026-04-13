class Pago:
    TARIFA_POR_HORA = 1000

    def __init__(self, registro):
        self.registro = registro
        self.monto = 0

    def calcular_monto(self):
        horas = self.registro.calcular_horas()
        self.monto = horas * self.TARIFA_POR_HORA
        return self.monto