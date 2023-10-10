primo = int(input ("Digite um número para saber se ele é primo:"))
contador = 0
divisores = []

for i in range(primo):

    if primo%(i+1) == 0:
        contador += 1
        divisores.append(i+1)
        
if contador == 2:
    print(f"O numero é primo divisivel por {divisores}")
else:
    print(f"O numero não é primo pois é divisivel por {divisores}")