codigo = int(input("Digite seu código:"))
altura = float(input("Digite sua altura:"))
peso = float(input("Digite seu peso:"))
parar = int(input("Digite 0 se deseja parar ou 1 para continuar:"))
altura_max = 0
altura_min = 300
peso_max = 0
peso_min = 300
contador = 0
codigo_peso_max = 0
codigo_peso_min = 0
codigo_altura_max = 0
codigo_altura_min = 0
soma_altura = 0 
soma_peso = 0 

while parar == 1:
    codigo = int(input("Digite seu código:"))
    altura = float(input("Digite sua altura:"))
    peso = float(input("Digite seu peso:"))
    parar = int(input("Digite 0 se deseja parar ou 1 para continuar:"))
    
    if peso > peso_max:
        peso_max = peso
        codigo_peso_max = codigo
    else:
        peso_max = peso_max
        
    if peso < peso_min:
        peso_min = peso
        codigo_peso_min = codigo
    else:
        peso_min = peso_min
        
    if altura < altura_min:
        altura_min = altura
        codigo_altura_min = codigo
    else:
        altura_min = altura_min
        
        
    if altura > altura_max:
        altura_max = altura
        codigo_altura_max = codigo
    else:
        altura_max = altura_max

    soma_altura += altura
    soma_peso += peso
    contador += 1

media_altura = soma_altura / contador
media_peso = soma_peso / contador
print(f"A média das alturas dos clientes é {media_altura} cm")
print(f"A média do peso dos clientes é {media_peso} Kg")
print(f"O cliente mais baixo tem o código {codigo_altura_min} e tem {altura_min} cm")
print(f"O cliente mais alto tem o código {codigo_altura_max} e tem {altura_max} cm")
print(f"O cliente menos pesado tem o código {codigo_peso_min} e pesa {peso_min} Kg")
print(f"O cliente mais pesado tem o código {codigo_peso_max} e pesa {peso_max} Kg")