def area_perimetro(raio):
    """Calcula a área e o perímetro de um círculo."""
    area = 3.14 * (raio)**2
    perimetro = 6.28 * (raio)

    print(f"A área do cícrulo é {area} e o perímetro é {perimetro: 0.2f}")

raio = float(input("Digite o raio do círculo:"))
area_perimetro(raio)