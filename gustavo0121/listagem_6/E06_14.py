respostas = []
contador = 0

respostas.append(input("Telefonou para a vítima? (s ou n)"))
respostas.append(input("Esteve no local do crime? (s ou n)"))
respostas.append(input("Mora perto da vítima? (s ou n)"))
respostas.append(input("Devia para a vítima? (s ou n)"))
respostas.append(input("Já trabalhou com a vítima? (s ou n)"))

for i in range(5):
    if respostas[i] == 's':
        contador += 1

if contador == 2:
    print("Suspeito(a)")
elif contador == 3 or contador == 4:
    print("Cúmplice")
elif contador == 5:
    print("Assasino")
else:
    print("Inocente")
        
