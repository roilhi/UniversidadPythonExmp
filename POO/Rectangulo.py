class Rectangulo:
    """ 
    Esta clase retorna el área de un 
    rectángulo, los parámetros de entrada serán 
    la base y la altura
    """
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def area(self):
        return self.base*self.altura

miBase = float(input('Proporciona la base '))
miAltura = float(input('Proporciona la altura '))
miRectangulo = Rectangulo(miBase,miAltura)
print(f'Area rectángulo: {miRectangulo.area()}')
# Reutilizando la clase y las variables generadas
miBase = float(input('Proporciona la base '))
miAltura = float(input('Proporciona la altura '))
miRectangulo2 = Rectangulo(miBase,miAltura)
print(f'Area rectángulo: {miRectangulo2.area()}')