pais_a = float(input("Digite a população do primeiro país:"))
taxa_a = float(input("Digite a taxa de crescimento do primeiro país (%):"))
pais_b = float(input("Digite a população do segundo país:"))
taxa_b = float(input("Digite a taxa de crescimento do segundo país (%):"))
ano = 0

while pais_a < pais_b:
    pais_a += pais_a * (taxa_a / 100)
    pais_b += pais_b* (taxa_b / 100)
    ano += 1

print(f"o País A levará {ano} anos para igualar a populaçao do país B")