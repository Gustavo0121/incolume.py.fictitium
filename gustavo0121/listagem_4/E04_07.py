turmas = int(input("Informe a quantidade de turmas:"))
media = 0 


for i in range(turmas):
    alunos = int(input("Quantos alunos tem nessa turma:"))
    while alunos > 40:
        print("Quantidade máxima de alunos permitida: 40")
        alunos = int(input("Quantos alunos tem nessa turma:"))
    media += alunos

media = media / turmas
print(f"O número médio de alunos por turma é {media: .2f}")