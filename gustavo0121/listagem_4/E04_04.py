contador1 = 0
contador2 = 0
contador3 = 0
contador4 = 0

while True:
    num = float(input("Digite um número ou um número negativo para parar:"))

    if num < 0:
        break
    elif num <= 25:
        contador1 += 1
    elif num <= 50:
        contador2 += 1
    elif num <= 75:
        contador3 += 1
    elif num <= 100:
        contador4 += 1
    else:
        print("Número inválido")

print(f"\nEntre 0-25 tem {contador1} números.")
print(f"\nEntre 25-50 tem {contador2} números.")
print(f"\nEntre 50-75 tem {contador3} números.")
print(f"\nEntre 75-100 tem {contador4} números.")