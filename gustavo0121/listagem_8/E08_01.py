def num_escada(num = int(input("Digite um número:"))):
    """Imprimir uma escada de números iguais."""
    contador = 1
    for i in range(1,num + 1):
        print(f"{contador * str(i)}")
        contador += 1


def num_escada_sequencial(num = int(input("Digite um número:"))):
    """Imprimir uma escada de números sequenciais."""
    lista_num = []
    for i in range(1,num + 1):
        lista_num.append(i)
        print(lista_num)
        

def soma(
    num1 = float(input("Digite um número:"))
    num2 = float(input("Digite um número:"))
    num3 = float(input("Digite um número:"))
    ):
    """Somar três números."""
    soma = num1 + num2 + num3
    print(f"A soma dos três números é: {soma}")


def positivo_negativo(num = int(input("Digite um número:"))):
    """Verificar se o número é positivo ou negativo."""
    if num > 0:
        print("Número positivo")
        return 'P'
    else:
        print("Número negativo")
        return 'N'


def soma_imposto(
    taxa_imposto = (float(input("Informe a taxa do imposto (em porcentagem):"))),
    custo = float(input("Informe o valor do produto:"))):
    """Calcular o valor de um produto sobre o imposto."""
    valor = ((taxa_imposto / 100) * custo) + custo
    print(f"Valor após impostos:{valor: .2f} R$")


def qtd_digitos(num = int(input("Digite um número inteiro:"))):
    """Calcular a quantidade de digitos."""
    print(f"Quantidade de dígitos: {len(str((num)))}")


def num_reverso(num = int(input("Digite um número inteiro:"))):
    """Reverter um número."""
    print(f"Número ao contrário: {str(num)[::-1]}")


def run():
    #num_escada()
    #num_escada()
    #soma()
    #positivo_negativo()
    #soma_imposto()
    #qtd_digitos()
    #num_reverso()