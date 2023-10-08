def palindromo(frase):
    """Verifica se uma palavra é um palíndromo."""
    if frase == frase[::-1]:
        print(f"{frase} é um palíndromo")
    else:
        print(f"{frase} não é um palíndromo")

frase = input("Digite uma frase:")
palindromo(frase)
    