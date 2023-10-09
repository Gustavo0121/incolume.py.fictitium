num1 = int(input("Digite um número inteiro:"))
num2 = int(input("Digite outro número inteiro:"))
soma = 0

if num2 > num1:
    for i in range(num1 +1,num2,1):
        soma += i
        print(i)
       
if num1 > num2:
    for i in range(num2 +1,num1,1):
        soma += i
        print(i)

print(f"A soma dos números é {soma}") 