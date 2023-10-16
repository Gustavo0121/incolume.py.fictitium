vetor = []
soma = 0
produto = 1

for i in range(5):
    vetor.append(int(input("Digite um número:")))
    soma += vetor[i]
    produto *= vetor[i]

print(f"Os números são {vetor}, a soma deles é: {soma} e a multiplicação é: {produto}")