notas = []
alunos_acima_media = 0

for i in range(10):
    media = 0
    notas = []
    print(f"Nota do aluno {i + 1}")
    for j in range(4):
        notas.append(float(input("Digite sua nota:")))
        media += notas[j]

    media = media / 4

    if media >= 7:
        alunos_acima_media += 1
        
        
print(f"O número de alunos a cima da média é: {alunos_acima_media}")