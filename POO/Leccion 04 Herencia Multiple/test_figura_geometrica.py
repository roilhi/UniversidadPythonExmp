from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

print('Creación Objeto Cuadrado'.center(50,'-'))
cuadrado1 = Cuadrado(lado=5,color='rojo')
cuadrado1.alto = 9
cuadrado1.ancho = 9
print(f'Cálculo del área cuadrado: {cuadrado1.calcular_area()}')
print(cuadrado1)
print('Creación Objeto Rectángulo'.center(50,'-'))
rectangulo1 = Rectangulo(ancho=3,alto=8,color='Verde')
rectangulo1.ancho = 15
print(f'Cálculo área rectángulo: {rectangulo1.calcular_area()}')
print(rectangulo1)
# MRO Method Resolution Order
#print(Cuadrado.mro())