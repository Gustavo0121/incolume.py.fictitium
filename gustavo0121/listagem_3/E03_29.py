soma = 0 
final = int(input("Digite o n° termo:"))
denominador = 1

for i in range(1, final + 1):
    print(f"{i}/{denominador}")

    if i < final and final > 1:
        print("+")
    else:
        print("=")

    soma += i / denominador
    denominador += 2
print(f"O resultado da soma é {soma: .2f}")