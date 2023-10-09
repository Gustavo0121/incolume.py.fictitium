num = int(input("Digite um número:"))
contador = num - 1
fatorial = 0

while contador > 1:
    fatorial = num * contador
    contador -= 1
    num = fatorial
    
print(f"Fatorial de {num}:\n {num}! = {fatorial}")