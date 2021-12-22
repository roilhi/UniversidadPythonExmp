def celsius_farenheit(celsius):
    return celsius*9/5+32

def farenheit_celsius(farenheit):
    return (farenheit-32)*5/9

t_celsius= float(input('Ingresa un valor de temperatura en Celsius '))
print(f'La temperatura {t_celsius} C equivale a {celsius_farenheit(t_celsius)} F')
t_farenheit= float(input('Ingresa un valor de temperatura en Farenheit '))
print(f'La temperatura {t_farenheit} F equivale a {farenheit_celsius(t_farenheit)} C')