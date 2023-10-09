impar = 0
par = 0

for i in range(10):
    num = int(input("Digite um número"))
    if num %2 == 0:
        par += 1
    else:
        impar += 1
        
        
print(f"Há {par} números pares e {impar} números ímpares")