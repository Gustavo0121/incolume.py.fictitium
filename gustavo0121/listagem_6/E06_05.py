vetor = []
vetor_par = []
vetor_impar = []
pares = []

for i in range(20):
    vetor.append(int(input("Digite um número inteiro:")))
    numero = vetor[i]
    if numero %2 == 0:
        vetor_par.append(numero)
    else:
        vetor_impar.append(numero)

print(f"Os números são: {vetor}")
print(f"Os números pares são: {vetor_par}")
print(f"Os números ímpares são: {vetor_impar}")