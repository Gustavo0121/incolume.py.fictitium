num = int(input("Digite um número:"))
contador = num - 1 

while contador > 1:
    num = num * contador
    contador -= 1
    
print(f"A resposta é {num}")