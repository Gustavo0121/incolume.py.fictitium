def peso_homem(altura):
    """Calcula e mostra o peso ideal da pessoa."""
    peso_ideal = (72.7 * altura) - 58
    print(f"O seu peso ideal é {peso_ideal: .1f}")


def peso_mulher(altura):
    """Calcula e mostra o peso ideal da pessoa."""
    peso_ideal = (62.1 * altura) - 44.7
    print(f"O seu peso ideal é {peso_ideal: .1f}")


sexo = input("Você é homem ou mulher? (M - Mulher, H - Homem):")
altura = float(input("Digite a sua altura:"))

if sexo == "M":
    peso_mulher(altura)
elif sexo == "H":
    peso_homem(altura)
