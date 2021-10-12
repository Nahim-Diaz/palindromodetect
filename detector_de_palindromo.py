def palindromo(palabra):
    palabra= palabra.replace(" ","")
    palabra= palabra.lower()
    palabrainver= palabra[::-1]
    if palabra == palabrainver:
        True
    else:
        False

def main():
    palabra= input("Escribe una frase o palabra: ")
    es_palindromo= palindromo(palabra)
    if es_palindromo ==True:
        print("Es un palindromo")
    else:
        print("No es palindromo")


if __name__ == "__main__":
    main()
