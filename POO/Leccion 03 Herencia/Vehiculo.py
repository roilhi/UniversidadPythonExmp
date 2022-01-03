class Vehiculo():
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    def __str__(self):
        return f'Vehículo: Color: {self.color} Ruedas: {self.ruedas}'

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
    def __str__(self):
        return f'Coche: {super().__str__()} Velocidad: {self.velocidad}'

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo
    def __str__(self):
        return f'Bicicleta:{super().__str__()} Tipo:{self.tipo}'

#miVehiculo = Vehiculo('rojo',4)

#print(miVehiculo)

#micoche = Coche('verde',4,275)

#print(micoche)

#miBici = Bicicleta('azul',2,'urbana')

#print(miBici)