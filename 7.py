#ejercicio 7

def suma_lista(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma

# Ejemplo de uso:
lista_numeros = [9, 2, 56, 3, 5]
suma_total = suma_lista(lista_numeros)
print("La suma de los números en la lista es:", suma_total)