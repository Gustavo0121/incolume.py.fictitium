def mes_extenso(mes):
    """Lista os meses e os dias do ano."""
    meses = [[],['Janeiro', 31], ['Fevereiro', 30], ['Março', 31],['Abril', 30], ['Maio', 31], ['Junho', 30], ['Julho', 31], ['Agosto', 31], ['Setembro', 30], ['Outubro', 31], ['Novembro', 30], ['Dezembro', 31]]
    
    dia, mes, ano = int(data[0]), int(data[1]), int(data[2])

    if 0 < mes < 13 and 0 < dia <= meses[mes][1] and 1910 < ano < 2023:
        print(f"Data de nascimento:{dia}/{mes}/{ano}")
        print(f"Você nasceu em {dia} de {meses[mes][0]} de {ano}")
    else:
        print("Data inválida")

data = str(input("Digite sua data de nascimento: DD/MM/YYYY:")).split("/")
mes_extenso(data)