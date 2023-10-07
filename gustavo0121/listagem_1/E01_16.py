def pintura(tamanho):
    """Calula a quantidade de latas e o preço para pintar uma área."""
    litros_lata = 18
    preco_lata = 80
    qtd_latas = (litros_necessarios / litros_lata)
    valor = (qtd_latas * preco_lata)

    print(f"A quantidade de latas a ser compradas é {qtd_latas: .1f} e o valor será de {valor: .2f}")

tamanho = float(input("Por favor, insira o tamanho da área em metros quadrados: "))
litros_necessarios = tamanho / 3

pintura(tamanho)