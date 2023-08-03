#ejercicio 11

def generar_lista():
    lista = []
    for numero in range(2, 101, 2):
        lista.append(numero)
    return lista

lista_numeros_pares = generar_lista_numeros_pares()

print("Lista de números pares entre 1 y 100:")
print(lista_numeros_pares)