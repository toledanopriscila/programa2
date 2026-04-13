class Mision:
    def __init__(self,nombre,fecha_lanzamiento,duracion,objetivo,estado,tipo_mision):
        self.nombre=nombre
        self.fecha_lanzamiento=fecha_lanzamiento
        self.duracion=duracion
        self.objetivo=objetivo
        self.estado=estado
        self.tipo_mision=tipo_mision
        
class Nave:
    def __init__(self, nombre, modelo, cantidad_tripulacion, estado_nave):
        self.nombre=nombre
        self.modelo=modelo
        self. cantidad_tripulacion=cantidad_tripulacion
        self.estado_nave
        
class Austronautas:
    def __init__(self, nombre, edad, nacionalidad, rol, especialidad):
        self.nombre=nombre
        self.edad=edad
        self.nacionalidad=nacionalidad
        self.rol=rol
        self.especialidad=especialidad
        
class ControlDeMision:
    def __init__(self, ubicacion, cantidad_personal, estado_operativo, jefe_de_mision):
        self.ubicacion=ubicacion
        self.cantidad_personal=cantidad_personal
        self.estado_operativo=estado_operativo
        self.jefe_de_mision=jefe_de_mision