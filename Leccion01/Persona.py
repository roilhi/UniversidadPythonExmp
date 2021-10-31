class Persona:
    # Se introducen argumentos variables para una tupla y un diccionario
    # primero deben ser tuplas y luego los diccionarios
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
        #self.valores = valores
        #self.terminos =  terminos
    # Encapsulando para que solo pueda accederse mediante el metodo
    # ya no son necesarios los paréntesis
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    @property
    def apellido(self):
        return self._apellido
    # Estableciendo para método set
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
    def __del__(self):
        print(f'Persona: {self._nombre} {self._apellido}')
#print(__name__)
# self equivale a this en java, C#
# Para que el código prueba no se ejecute en el otro módulo
if __name__ == '__main__':
    persona1 = Persona('Juan','Perez',28)
    # Variable de solo lectura, marcará error
    persona1.nombre = "Juan Carlos"
    persona1.apellido = "Lara"
    persona1.edad = 30
    persona1.mostrarDetalle()
    print(__name__)