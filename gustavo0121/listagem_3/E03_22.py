qtd_notas = int(input("Quantos notas quer digitar:"))
contador = 0
soma = 0

while contador < qtd_notas:
    notas = float(input("Digite uma nota:"))
    soma += notas
    contador += 1 

media = soma / qtd_notas
print(f"A média é: {media}")
