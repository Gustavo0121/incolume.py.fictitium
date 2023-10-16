frase = []
contador = 0
vogais = ('a','e','i','o','u')

for i in range(10):
    frase.append(input("Digite um caracter:"))
    caracter = frase[i]
    if caracter not in vogais:
        contador += 1

print(contador)