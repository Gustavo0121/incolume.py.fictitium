final = int(input("Digite o n° termo:"))
contador = 0 
h = 1
denominador = 2
result = 1

while contador < final - 1:
    result += h / denominador
    denominador += 1
    contador += 1

print(f"O resultado é: {result: .2f}")