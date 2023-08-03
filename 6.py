#ejercicio 6

def fahrenheit_a_celsius(grados_fahrenheit):
    grados_celsius = (grados_fahrenheit - 32) * 5/9
    return grados_celsius


temperatura_fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))
temperatura_celsius = fahrenheit_a_celsius(temperatura_fahrenheit)
print("La temperatura en grados Celsius es:", temperatura_celsius)