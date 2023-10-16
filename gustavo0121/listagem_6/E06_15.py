num = []
contador_media = 0
contador_abaixo = 0

while True:
    valor = int(input("Digite um número:"))
    
    if valor == -1:
        break
    
    num.append(valor)

soma = sum(num)
media = soma / len(num)

for i in range(len(num)):
    if num[i] > media:
        contador_media += 1 
    if num[i] < 7:
        contador_abaixo += 1

print(f"A quantidade de valores informados é de: {len(num)}")
print(f"Os valores informados são: {num}")
print(f"Os valores informados em ordem inversa são:{num[::-1]}")
print(f"A soma dos valores é: {soma}")
print(f"A média dos valores é: {media: .2f}")
print(f"A quantidade de valores acima da média é: {contador_media}")
print(f"A quantidade de valores abaixo de sete é: {contador_abaixo}")
print("Programa encerrado.")

