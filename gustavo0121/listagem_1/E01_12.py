def peso(altura):
    """Calcula e mostra o peso ideal da pessoa."""
    peso_ideal = (72.7 * altura) - 58
    print(f"O seu peso ideal é {peso_ideal: .1f}")

altura = float(input("Digite a sua altura:"))
peso(altura)