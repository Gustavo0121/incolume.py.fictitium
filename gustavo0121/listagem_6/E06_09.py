vetor_a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
quadrado = 0
soma = 0

for i in range(10):
    quadrado += vetor_a[i] * vetor_a[i]

print(f"A soma dos quadrados dos elementos do vetor é: {quadrado}")