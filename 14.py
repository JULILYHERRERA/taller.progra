#ejercicio 14

def media_aritmetica(lista):
    suma = sum(lista)
    cantidad_elementos = len(lista)
    media = suma / cantidad_elementos
    return media

# Ejemplo de uso:
lista_numeros = [18, 20, 38, 20, 50]
media_aritmetica = media_aritmetica(lista_numeros)
print("La media aritmética es:", media_aritmetica)