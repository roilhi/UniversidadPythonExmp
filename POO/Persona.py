class Persona:
    # Se introducen argumentos variables para una tupla y un diccionario
    # primero deben ser tuplas y luego los diccionarios
    def __init__(self, nombre, apellido, edad, *valores, **terminos):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.valores = valores
        self.terminos =  terminos
    #Se crea un nuevo método para la clase    
    def mostrarDetalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad} {self.valores} {self.terminos}')
# self equivale a this en java, C#
persona1 = Persona('Juan','Perez',28, '44423364', 2,3,5, m='manzana', p='pera')
Persona.mostrarDetalle(persona1)
# Es posible agregar atributos al objeto, sin
#embargo no se comparten al otro objeto
#persona1.telefono = '55441122'
#print(persona1.telefono)

#persona1.mostrarDetalle()
#print(persona1.nombre)
#print(persona1.apellido)
#print(persona1.edad)

#print(f'Objeto Persona 1: {persona1.nombre} {persona1.apellido} {persona1.edad}')

persona2 = Persona('Karla','Gomez',30)
persona2.mostrarDetalle()
#Nos marca error porque no contiene el atributo de telefono
#print(persona2.telefono)
#print(persona2.nombre)
#print(persona2.apellido)
#print(persona2.edad)
#print(f'Objeto Persona 2: {persona2.nombre} {persona2.apellido} {persona2.edad}')
#class Persona:
#    def __init__(self):
#        self.nombre ='Juan'
#        self.apellido ='Perez'
#        self.edad = 28

#persona1 = Persona()
#print(persona1.nombre)
#print(persona1.apellido)
#print(persona1.edad)
#def __str__(self):

# modificar los atributos de un objeto una vez creado
#persona1.nombre = 'Juan Carlos'
#persona1.apellido = 'Juarez'
#persona1.edad = 25

#print(f'Objeto Persona 1: {persona1.nombre} {persona1.apellido} {persona1.edad}')

#persona2.nombre = 'Laura'
#persona2.apellido = 'Garza'
#persona2.edad = 45
#print(f'Objeto Persona 2: {persona2.nombre} {persona2.apellido} {persona2.edad}')