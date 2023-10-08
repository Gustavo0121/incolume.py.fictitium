numero = str(input('Digite o n° do telefone: '))

while len(numero) > 8 or len(numero) < 7:
    print('O número precisa ter 8 ou 7 digitos')
    numero = str(input('Digite o n° do telefone: '))
print(len(numero))

if len(numero) == 7:
    print ('Telefone possui 7 digitos. Vou acrescentar o digito tres na frente.')
    numero = '3' + numero
    print('Telefone corrigido: ',numero)
else:
    print("O número tem 8 dígitos e está correto")