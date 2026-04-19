#POLIMORFISMO

class Mision:
    def describir(self):
        print("Misión general")

class MisionExploracion(Mision):
    def describir(self):  # POLIMORFISMO
        print("Misión de exploración espacial")

class MisionRescate(Mision):
    def describir(self):  # POLIMORFISMO
        print("Misión de rescate")
        
m1 = MisionExploracion()
m2 = MisionRescate()

m1.describir()
m2.describir()

        
#ENCAPSULAMIENTO

class Nave:
    def __init__(self, nombre, estado_nave):
        self.nombre = nombre
        self.__estado_nave = estado_nave

    @property
    def estado_nave(self):
        return self.__estado_nave

    @estado_nave.setter
    def estado_nave(self, nuevo_estado):
        if nuevo_estado != "":
            self.__estado_nave = nuevo_estado
            
nave = Nave("Apollo", "Activa")

print(nave.estado_nave)   # getter

nave.estado_nave = "En mantenimiento"  # setter
print(nave.estado_nave)
            

#HERENCIA
        
class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

class Austronauta(Persona):
    def __init__(self, nombre, edad, nacionalidad, rol, especialidad):
        super().__init__(nombre, edad, nacionalidad)
        self.rol=rol
        self.especialidad=especialidad
        
a1 = Austronauta("Juan", 30, "Argentina", "Piloto", "Ingeniero")

print(a1.nombre)
print(a1.rol)
        
#ABSTRACCION
        
from abc import ABC, abstractmethod

class ControlDeMision(ABC):
    def __init__(self, ubicacion):
        self.ubicacion = ubicacion

    @abstractmethod
    def operar(self):
        pass
    
class ControlNASA(ControlDeMision):
    def operar(self):
        print(f"Control en {self.ubicacion} operando misiones")
        
c1 = ControlNASA("EE.UU")
c1.operar()