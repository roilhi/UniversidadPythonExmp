def factorial(numero):
    if numero ==1:
        return 1
    else:
        return numero * factorial(numero-1)
numero = 5
resultado = factorial(numero)
print(f'El factorial de {numero} es: {resultado}')
#def desplegarNombres(nombres):
#    for nombre in nombres:
#        print(nombre)

#nombres = ['Juan','Karla', 'Guillermo']

#desplegarNombres(nombres)
#desplegarNombres('Carlos')
#desplegarNombres((10,11))
#desplegarNombres([10,11])

#def ListarTerminos(**terminos):
#    for llave, valor in terminos.items():
#        print(f'{llave}: {valor}')
#
#ListarTerminos(IDE='Integrated Development Environment',PK='Primary Key')

#ListarTerminos(DBMS='Database management System')

#def miFuncion(nombre, apellido):
#    print('Saludos desde mi función')
#    print(f'Nombre: {nombre}, Apellido: {apellido}')

#miFuncion('Juan', 'Pérez')
#miFuncion('Karla', 'Lara')

#def sumar(a=0, b=0) -> int:
#    return a+b
#resultado = sumar()
#print(f'Resultado sumar: {resultado}')
#print(f'Resultado sumar: {sumar(2,8)}')

#def ListarNombres(*nombres):
#    for nombre in nombres:
#        print(nombre)

#ListarNombres('Juan', 'Felipe' , 'Karla', 'María', 'Ernesto')

#ListarNombres('Laura','Carlos','Juan','Erick','Felipe')

#def SumaNumeros(*numeros):
#    suma = 0
#    for numero in numeros:
#        suma += numero
#    return suma
#print(SumaNumeros(1,2,3))

#def MultiplicaNumeros(*args):
#    mult = 1
#    for valor in args:
#        mult *=valor 
#    return mult 

#print(MultiplicaNumeros(1,2,3,4))
