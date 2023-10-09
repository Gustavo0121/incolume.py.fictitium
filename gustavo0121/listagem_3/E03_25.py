numero_maior = 0
altura_maior = 0
numero_menor = 0
altura_menor = 500

for i in range(1,11):
    altura = int(input("Digite a altura do aluno:"))

    if altura > altura_maior:
        altura_maior = altura
        numero_maior = i
    if altura < altura_menor:
        altura_menor = altura
        numero_menor = i

print(f"O aluno mais alto é o {numero_maior}° com {altura_maior} cm")
print(f"O aluno mais baixo é o {numero_menor}° com {altura_menor} cm")