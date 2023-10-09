tabuada = int(input("Digite um número para ver a tabuada:"))
contador = 0
while contador <= 9:
    contador += 1
    resultado = tabuada * contador
    print(f"{tabuada} X {contador} = {resultado}")