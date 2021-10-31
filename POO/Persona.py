class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

persona1 = Persona('Juan','Perez',28)
#print(persona1.nombre)
#print(persona1.apellido)
#print(persona1.edad)

print(f'Objeto Persona 1: {persona1.nombre} {persona1.apellido} {persona1.edad}')

persona2 = Persona('Luis','Ramos',17)
#print(persona2.nombre)
#print(persona2.apellido)
#print(persona2.edad)
print(f'Objeto Persona 2: {persona2.nombre} {persona2.apellido} {persona2.edad}')
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