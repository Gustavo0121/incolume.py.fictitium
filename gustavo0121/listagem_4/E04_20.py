print('\n| Especificação |     Código     | Valor | \n| Cachorro quente | 100 | 1,20R$| \n'
      '| Bauru Simples |  101  | 1,30R$|\n| Bauru com ovo |  102  | 1,50R$|\n| Hamburguer |  103  | 1,20R$| \n'
      '| Chessburguer | 104 | 1,70R$|\n| Suco |    105    | 2,20R$| \n| Refrigerante |  106  | 1,00R$|\n'
      '\n Para sair digite 999')
total = 0
preco = 0

while True:
    codigo = int(input('Informe o codigo: '))
    if(codigo == 999):
        break
    quantidade = int(input('Informe a quantidade: '))
    if codigo == 100:
        preco = 1.20
    elif codigo == 101:
        preco = 1.30
    elif codigo == 102:
        preco = 1.50
    elif codigo == 103:
        preco = 1.20
    elif codigo == 104:
        preco = 1.70
    elif codigo == 105:
        preco = 2.20
    elif codigo == 106:
        preco = 1
    else:
        print('Codigo invalido')
    
    total += preco * quantidade
    
print(total, 'reais')