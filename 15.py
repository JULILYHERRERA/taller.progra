#ejercicio 15
def es_palindromo(cadena):
    cadena = cadena.replace(" ", "").lower()
    return cadena == cadena[::-1]

def main():
    texto = input("Ingresa una cadena de texto: ")
    if es_palindromo(texto):
        print("Es un palíndromo.")
    else:
        print("No es un palíndromo.")

if __name__ == "__main__":
    main()