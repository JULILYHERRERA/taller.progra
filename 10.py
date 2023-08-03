#ejercicio 10

def factorial(numero):
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    return factorial

numero_dado = int(input("Ingrese un número entero : "))
resultado_factorial = factorial(numero_dado)
print("El factorial de", numero_dado, "es:", resultado_factorial)