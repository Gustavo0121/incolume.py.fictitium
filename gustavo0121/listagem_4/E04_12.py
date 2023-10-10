primo = int(input ("Digite um número para saber se ele é primo:"))
contador = 0

for i in range(primo):

    if primo%(i+1) == 0:
        contador += 1
        
if contador == 2:
    print("O numero é primo")
else:
    print ("O numero não é primo")