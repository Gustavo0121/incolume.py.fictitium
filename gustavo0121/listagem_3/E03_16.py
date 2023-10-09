fibonacci = int(input("Digite o n° termo:")) 
x = 1
y = 1

for i in range(fibonacci):
    print (x)
    soma=x+y
    x = y
    y = soma
