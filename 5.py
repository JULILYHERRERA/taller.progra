#ejercicio 5

def fahrenheit_to_celsius():
    try:
        fahrenheit = float(input("Ingresa la temperatura en Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit:.2f} grados Fahrenheit son {celsius:.2f} grados Celsius.")
    except ValueError:
        print("no es valido.")

fahrenheit_to_celsius()