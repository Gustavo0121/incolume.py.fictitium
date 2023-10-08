def up_contrary(nome):
    """Inverte e deixa em caixa-alta o nome da pessoa."""
    nome_contrario = nome[::-1]
    print(f"o seu nome ao contrário em caixa alta é:{nome_contrario.upper()}")

nome = input("Digite seu nome:")
up_contrary(nome)
