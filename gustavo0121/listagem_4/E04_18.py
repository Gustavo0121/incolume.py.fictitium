indice_maior = 0
codigo_indice_maior = 0
indice_menor = 100000000000000
codigo_indice_menor = 0
veiculos = 0
cidades_menos_de_2000 = 0
acidentes_cidades_menos_de_2000 = 0

for i in range(5):
    codigo = int(input("Digite o codigo da cidade: "))
    veiculos = int(input("Digite o número de veículos de passeio: "))
    acidentes = int(input("Digite o número de acidentes: "))

    if acidentes > indice_maior:
        indice_maior = acidentes
        codigo_indice_maior = codigo
    
    if acidentes < indice_menor:
        indice_menor = acidentes
        codigo_indice_menor = codigo

    veiculos += veiculos

    if veiculos < 2000:
        cidades_menos_de_2000 += 1
        acidentes_cidades_menos_de_2000 += acidentes

print(f"A cidade com maior índice de acidentes é a {codigo_indice_maior} com {indice_maior} acidentes")
print(f"A cidade com menor índice de acidentes é a {codigo_indice_menor} com {indice_menor} acidentes")
print(f"A média de veículos é de {veiculos / 5: .2f}")
print(f"A média de acidentes em cidades com menos de 2000 veículos é de {acidentes_cidades_menos_de_2000/cidades_menos_de_2000:.2f}")