peso = float(input("Digite seu peso (em kilogramas):"))
altura = float(input("Digite sua altura (em centímetros):"))
imc = peso / ((altura / 100) ** 2)

if imc < 18.5:
    print("Você está abaixo do peso.")
elif 18.5 < imc < 24.9:
    print("Seu peso está normal.")
elif 25 < imc < 29.9:
    print("Você está em sobrepeso.")
elif 30 < imc < 34.9:
    print("Seu nível de obesidade é de grau 1.")
elif 35 < imc < 39.9:
    print("Seu nível de obesidade é de grau 2.")
elif imc > 40:
    print("Seu nível de obesidade é de grau 3.")