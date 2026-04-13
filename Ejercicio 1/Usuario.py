class Usuario:
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni

    def mostrar_datos(self):
        return f"Nombre: {self.nombre} - DNI: {self.dni}"


class Administrador(Usuario):
    def __init__(self, nombre, dni, contraseña):
        super().__init__(nombre, dni)
        self.contraseña = contraseña

    def gestionar_estacionamiento(self):
        return f"El administrador {self.nombre} está gestionando el estacionamiento."


# Crear administrador
admin1 = Administrador("Carlos", "30111222", "admin123")
print(admin1.mostrar_datos())
print(admin1.gestionar_estacionamiento())


class Cliente(Usuario):
    def __init__(self, nombre, dni, telefono):
        super().__init__(nombre, dni)
        self.telefono = telefono

    def solicitar_estacionamiento(self):
        return f"El cliente {self.nombre} solicita un lugar para estacionar."
    
# Crear cliente
cliente1 = Cliente("Lucía", "40222333", "2615557890")
print(cliente1.mostrar_datos())
print(cliente1.solicitar_estacionamiento())
