def produto(num1, num2):
    """Calcula e mostra o produto do dobro do primeiro com metade do segundo."""
    resultado = (num1 * 2) * (num2 / 2)
    print(
        f"O produto do dobro do primeiro com metade do segundo é {resultado}")


def soma(num1, num3):
    """Calcula e mostra a soma do triplo do primeiro com o terceiro."""
    resultado2 = num1 * 3 + num3
    print(f"a soma do triplo do primeiro com o terceiro é {resultado2}")


def exponente(num3):
    """Calcula e mostra o terceiro elevado ao cubo."""
    resultado3 = num3**3
    print(f"o terceiro elevado ao cubo é {resultado3: .2f}")


num1 = int(input("Digite um número inteiro:"))
num2 = int(input("Digite outro número inteiro:"))
num3 = float(input("Digite um número real:"))

produto(num1, num2)
soma(num1, num3)
exponente(num3)
