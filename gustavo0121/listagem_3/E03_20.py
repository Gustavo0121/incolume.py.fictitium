qtd_numeros = int(input("Quantos números quer digitar:"))
num = int(input("Digite um número:"))
maior = num
menor = num 
soma = num
contador = 0

if num < 1001:
    while contador < qtd_numeros - 1:
        num = int(input("Digite um número:"))
        soma += num
        contador += 1

        if num > maior:
            maior = num
        elif num < menor:
            menor = num

    print(f"O maior número é {maior}, o menor é {menor} e a soma é {soma}")
else:
    print("Numéro tem que ser menor que 1001")
