cds = int(input("Informe a quantidade de cds:"))
media = 0

for i in range(cds):
    preco = int(input("Quantos custou esse cd:"))
    media += preco

media = media / cds
print(f"Você comprou {cds} cds e o valor médio de cada cd foi de {media: .2f} R$")