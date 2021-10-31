# Importando una clase de un archivo
# Cuando se quiera importar todo
# from Persona import *
from Persona import Persona
#if __name__ == '__main__':
print('Creacion objetos'.center(50,'-'))
persona1 = Persona('Karla', 'Gomez',30)
persona1.mostrarDetalle()
print('Eliminación objetos'.center(30,'-'))
del persona1


