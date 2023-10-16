idade = []
altura = []
aluno_13 = []
contador = 0 

for i in range(30):
    print(f"Aluno {i + 1}")
    idade.append(int(input("Digite sua idade:")))
    altura.append(int(input("Digite sua altura:")))
    if idade[i] > 13:
        aluno_13.append(altura[i])
        
media = sum(aluno_13) / len(aluno_13)

for i in range(len(aluno_13)):
    if aluno_13[i] < media:
        contador += 1 

print(f"A quantidade de alunos com mais de 13 anos e com altura inferior a média é {contador}")