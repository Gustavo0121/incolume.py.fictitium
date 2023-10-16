voto_jogadores = []
numero_votados = []
jogadores_votados = []

def percent(votos_individual, total_votos):
    """Calcula o percentual de votos de cada jogador."""
    porcentagem = (votos_individual / total_votos) * 100
    return porcentagem


while True:
    numero = int(input("Digite o número do jogador ou 0 para encerrar:"))

    if numero < 0 or numero > 23:
        print("O número tem que ser entre 1 e 23")
        continue
    if numero == 0:
        break

    voto_jogadores.append(numero)

contador = 1 

for i in range(23):
    if contador not in voto_jogadores:
        contador += 1
        continue
    else:
        jogadores_votados.append(voto_jogadores.count(contador))
        numero_votados.append(contador)
        print(f"\nVotos para o jogador camisa n° {contador} = {voto_jogadores.count(contador)}")
        print(f"\nPercentual de votos: {round(100 * voto_jogadores.count(contador) / len(voto_jogadores), 2)} %")
        contador += 1

mais_votado = jogadores_votados.index(max(jogadores_votados))
print(f"\nO jogador mais votado foi o n° {numero_votados[mais_votado]} com {jogadores_votados[mais_votado]} votos")
print(f"Ganhou com {round(100 * jogadores_votados[mais_votado] / len(voto_jogadores), 2)} % dos votos")


