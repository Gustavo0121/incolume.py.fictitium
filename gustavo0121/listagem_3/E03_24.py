qtd_temp = int(input("Quantas temperaturas deseja informar:"))
temp = float(input("Digite uma temperatura:"))
maior_temp = temp
menor_temp = temp
contador = 0
soma = 0

while contador < qtd_temp - 1:
    soma += temp
    temp = float(input("Digite uma temperatura:"))
    contador += 1

    if temp > maior_temp:
        maior_temp = temp
    elif temp < menor_temp:
        menor_temp = temp

print(f"A maior temperatura é {maior_temp}, a menor é {menor_temp} e a média das temperaturas é de {soma / qtd_temp}")
