def fahrenheit(graus_fahrenheit):
    """Transforma Fahrenheit em Celsius"""
    celsius = 5 * ((graus_fahrenheit - 32) / 9)
    print(f"{graus_fahrenheit} °F em Celsius é {celsius: .1f} °C")


graus_fahrenheit = float(input("Digite a temperatura em Fahrenheit"))

fahrenheit(graus_fahrenheit)
