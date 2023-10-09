base = int(input("Digite a base:"))
expoente = int(input("Digite o expoente:"))
contador = 1

for i in range(expoente):
    contador = contador * base
print(f"O primeiro número elevado ao segundo é: {contador}")