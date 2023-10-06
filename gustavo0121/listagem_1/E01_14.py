def multa(peso_peixes):
    """Calcula amulta de acordo com o peso excedido."""
    excedido = peso_peixes - 50
    valor = excedido * 4
    print(f"O peso excedido é: {excedido}")
    print(f"o valor da multa é {valor}")

peso_peixes = float(input("Digite o peso de peixes:"))

if peso_peixes > 50:
    multa(peso_peixes)
else:
    print("O peso está dentro do limite")