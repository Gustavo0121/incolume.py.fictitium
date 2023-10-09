num1 = float(input("Digite o primeiro número:"))
num2 = float(input("Digite o segundo número:"))
num3 = float(input("Digite o terceiro número:"))
num4 = float(input("Digite o quarto número:"))
num5 = float(input("Digite o quinto número:"))

if num1 > num2 and num1 > num3 and num1 > num4 and num1 > num5:
    print(f"O maior número é o primeiro: {num1}")

if num2 > num1 and num2 > num3 and num2 > num4 and num2 > num5:
    print(f"O maior número é o segundo: {num2}")

if num3 > num2 and num3 > num1 and num3 > num4 and num3 > num5:
    print(f"O maior número é o terceiro: {num3}")

if num4 > num2 and num4 > num3 and num4 > num1 and num4 > num5:
    print(f"O maior número é o quarto: {num4}")

if num5 > num2 and num5 > num3 and num5 > num4 and num5 > num1:
    print(f"O maior número é o quinto: {num5}")
    