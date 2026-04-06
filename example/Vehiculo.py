

class Vehiculo:
    def __init__(self, color, marca, patente):
        self.color=color
        self.marca=marca
        self.patente=patente
    def avanzar(self):
        return f"El vehiculo {self.color} de color {self.marca} con patente {self.patente} avanza cuando ingresa a la playa de estacionamiento "
    def estacionar(self):
        return f"El vehiculo {self.color} de color {self.marca} con patente {self.patente} estaciona cuando ingresa a la playa de estacionamiento "
vehiculo_uno=Vehiculo("Negro","Honda", "ACC03")
print (vehiculo_uno.avanzar())
print (vehiculo_uno.estacionar())
vehiculo_dos=Vehiculo("Rojo", "Ford", "AV15")
print (vehiculo_dos.avanzar())
print (vehiculo_dos.estacionar())
vehiculo_tres=Vehiculo("Blanco","Peugeot", "FD45")
print (vehiculo_tres.avanzar())
print (vehiculo_tres.estacionar())
