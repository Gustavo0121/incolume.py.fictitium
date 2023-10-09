num = int(input("Digite um número:"))

while num > 16:
    print("O número tem que ser menor que 16")
    num = int(input("Digite um número:")) 
else:
    contador = num - 1
    while contador > 1:
        num = num * contador
        contador -= 1

print(f"O fatorial é {num}")
