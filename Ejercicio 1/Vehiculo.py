class Vehiculo:
    def __init__(self, color, marca, patente):
        self.color = color
        self.marca = marca
        self.patente = patente

    def avanzar(self):
        return f"El vehículo {self.marca} de color {self.color} con patente {self.patente} avanza cuando ingresa a la playa de estacionamiento"

    def estacionar(self):
        return f"El vehículo {self.marca} de color {self.color} con patente {self.patente} estaciona cuando ingresa a la playa de estacionamiento"


# ----- PRUEBA DE VEHICULOS -----
vehiculo_uno = Vehiculo("Negro", "Honda", "ACC03")
print(vehiculo_uno.avanzar())
print(vehiculo_uno.estacionar())

vehiculo_dos = Vehiculo("Rojo", "Ford", "AV15")
print(vehiculo_dos.avanzar())
print(vehiculo_dos.estacionar())

vehiculo_tres = Vehiculo("Blanco", "Peugeot", "FD45")
print(vehiculo_tres.avanzar())
print(vehiculo_tres.estacionar())


class Auto(Vehiculo):
    def __init__(self, color, marca, patente, puertas):
        super().__init__(color, marca, patente)
        self.puertas = puertas

    def avanzar(self):
        return f"El auto {self.color} de color {self.marca} con patente {self.patente} y {self.puertas} puertas avanza cuando ingresa a la playa de estacionamiento"

    def estacionar(self):
        return f"El auto {self.color} de color {self.marca} con patente {self.patente} y {self.puertas} puertas estaciona cuando ingresa a la playa de estacionamiento"


# ----- PRUEBA DE AUTOS -----
auto1 = Auto("Rojo", "Fiat", "CDH06", 4)
print(auto1.avanzar())
print(auto1.estacionar())

auto2 = Auto("Rojo", "Ford", "AV15", 4)
print(auto2.avanzar())
print(auto2.estacionar())

auto3 = Auto("Blanco", "Peugeot", "FD45", 4)
print(auto3.avanzar())
print(auto3.estacionar())

class Motos(Vehiculo):
    def __init__(self, color, marca, patente, cilindradas):
        super().__init__(color, marca, patente)
        self.silindradas=cilindradas
    def avanzar(self):
        return f"La moto color {self.color} marca {self.marca} con patente {self.patente} y {self.silindradas} silindradas avanza cuando ingresa a la playa de estacionamiento"
    def estacionar(self):
        return f"La moto color {self.color} marca {self.marca} con patente {self.patente} y {self.silindradas} silindradas estaciona cuando ingresa a la playa de estacionamiento"
    
# ----- PRUEBA DE MOTOS -----
moto1 = Motos("Roja", "Honda wave", "CDH06", 110)
print(moto1.avanzar())
print(moto1.estacionar())

moto2= Motos("Negra", "BM", "AV15", 300)
print(moto2.avanzar())
print(moto2.estacionar())

moto3= Motos("Blanca", "KTM", "FD45", 250)
print(moto3.avanzar())
print(moto3.estacionar())