class Cubo:
    def __init__(self, ancho, profundo, alto):
        self.ancho = ancho
        self.profundo = profundo
        self.alto = alto
    def volumen(self):
        return self.ancho*self.profundo*self.alto
miAncho = float(input('Ingrese valor para el ancho '))
miProf = float(input('Ingrese valor para profundidad '))
miAlto = float(input('Ingrese valor para el alto '))
miCubo = Cubo(miAncho,miProf,miAlto)
print(f'El volumen del cubo es: {miCubo.volumen()}')