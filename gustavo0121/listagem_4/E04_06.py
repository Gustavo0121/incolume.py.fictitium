eleitores = int(input("Informe a quantidade de eleitores:"))
candidato1 = 0
candidato2 = 0
candidato3 = 0

for i in range (eleitores):
    voto = int(input("Qual é o seu voto (1 - Candidato1, 2 - Candidato2, 3 - Candidato3):"))

    if voto == 1:
        candidato1 += 1
    elif voto == 2:
        candidato2 += 1
    elif voto == 3:
        candidato3 += 1

print(f"O candidato1 teve {candidato1} votos")
print(f"O candidato2 teve {candidato2} votos")
print(f"O candidato3 teve {candidato3} votos")

    