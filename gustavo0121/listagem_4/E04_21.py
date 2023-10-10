lula = 0
bolsonaro = 0
jango = 0
fhc = 0
nulos = 0
branco = 0
qtd_votos = 0

while True:
    voto = int(input("Qual é o seu voto (0 para encerrar, 1 - Lula, 2 - Bolsonaro, 3 - Jõao Goulart (Jango), 4 - Fernando Henrique Collor (FHC), 5 - Nulo, 6 - Branco):"))
    if voto == 0:
        break

    if voto == 1:
        lula += 1
    elif voto == 2:
        bolsonaro += 1
    elif voto == 3:
        jango += 1
    elif voto == 4:
        fhc += 1
    elif voto == 5:
        nulos += 1
    elif voto == 6:
        branco += 1
    qtd_votos += 1
    
nulo_percent = nulos / qtd_votos
branco_percent = branco / qtd_votos

print(f"Lula teve {lula} votos")
print(f"Bolsonaro teve {bolsonaro} votos")
print(f"Jango teve {jango} votos")
print(f"FHC teve {fhc} votos")
print(f"Tiveram {nulos} votos nulos e {branco} votos brancos")
print(f"A percentagem de votos nulos é {nulo_percent * 100: .1f} %")
print(f"A percentagem de votos brancos é {branco_percent * 100: .1f} %")

    