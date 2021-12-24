class Persona:
    # Se introducen argumentos variables para una tupla y un diccionario
    # primero deben ser tuplas y luego los diccionarios
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre # El atributo nombre es ahora privado (private), sin embargo es solo un indicador el guion bajo
        self._apellido = apellido
        self._edad = edad
    @property   #Decorador que encapsula para acceder al método como si fuera un atributo (get)
    def nombre(self):
        return self._nombre
    @nombre.setter   #Para poder modificar el valor del método (set), si se comenta será variable de solo lectura
    def nombre(self, nombre):
        self._nombre = nombre
    @property
    def apellido(self):
        return self._apellido
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido
    @property
    def edad(self):
        return self._edad
    @edad.setter
    def edad(self, edad):
        self._edad = edad 
    #Se crea un nuevo método para la clase    
    def mostrarDetalle(self):
        print(f'Persona: {self._nombre} {self._apellido} {self._edad}')
# self equivale a this en java, C#
persona1 = Persona('Juan','Perez',28)
persona1.nombre = 'Juan Carlos'
persona1.apellido = 'Lara'
persona1.edad = 30
persona1.mostrarDetalle()