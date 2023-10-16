notas = []
media = 0

for i in range(4):
    notas.append(float(input("Digite sua nota:")))
    media += notas[i]

media = media / 4
print(f"As notas são {notas} e a média é {media}")