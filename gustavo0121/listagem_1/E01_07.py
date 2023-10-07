def area_quadrado(altura):
    """Calcula o dobro da altura de um quadrado."""
    area = altura**2
    print(f"O dobro da área é: {area * 2}")

altura = float(input("Digite a altura do quadrado:"))
area_quadrado(altura)
