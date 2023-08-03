#ejercicio 9

def invertir_lista(lista):
    lista_invertida = lista[::-1]
    return lista_invertida

lista_ori = [8, 12, 3, 42, 5]
lista_i = invertir_lista(lista_ori)

print("Lista normal:", lista_original)
print("Lista invertida:", lista_i)