def celsius(graus_celsius):
    """Transforma Celsius em Fahrenheit."""
    fahrenheit = graus_celsius * 1.8 + 32
    print(f"{graus_celsius: .1f}°C é {fahrenheit} °F em Fahrenheit ")


graus_celsius = float(input("Digite a temperatura em Celsius"))

celsius(graus_celsius)
