temperaturas = []
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro','Dezembro']

for i in range(12):
    print(f"Temperatura média do mês {i + 1}")
    temperaturas.append(float(input("Digite a temperatura média do mês:")))

media = sum(temperaturas) / len(temperaturas)

for i in range(12): 
    if temperaturas[i] > media:
        print(f"{i + 1} - {meses[i]}")