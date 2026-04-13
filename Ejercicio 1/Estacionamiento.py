from registro import Registro
from pago import Pago

class Estacionamiento:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.registros = []

    def ingresar(self, vehiculo):
        if len(self.registros) < self.capacidad:
            registro = Registro(vehiculo)
            self.registros.append(registro)
            print("Vehículo ingresado.")
        else:
            print("Estacionamiento lleno.")

    def retirar(self, patente):
        for registro in self.registros:
            if registro.vehiculo.patente == patente:
                registro.registrar_salida()
                pago = Pago(registro)
                print("Monto a pagar:", pago.calcular_monto())
                self.registros.remove(registro)
                print("Vehículo retirado.")
                return
        print("Vehículo no encontrado.")