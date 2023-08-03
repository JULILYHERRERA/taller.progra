#ejercicio 8

def maximo_minimo(lista):
    maximo = max(lista)
    minimo = min(lista)
    return maximo, minimo

lista_numeros = [7, 1, 7, 2, 9, 3]
maximo_numero, minimo_numero = maximo_minimo(lista_numeros)

print("El número más grande es:", maximo_numero)
print("El número más pequeño es:", minimo_numero)