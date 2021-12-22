def calcular_total(inicial,tasa_impuestos):
    return inicial*(1+(tasa_impuestos/100))

#Ejemplo aplicación
valor_inicial = float(input('Ingrese una cantidad inicial '))
tasa = float(input('Ingrese el valor de la tasa de impuestos (0-100)% '))
final = calcular_total(1000,16)
print(f'El valor final es: {final} al agregar una tasa del {tasa}% de impuestos')
