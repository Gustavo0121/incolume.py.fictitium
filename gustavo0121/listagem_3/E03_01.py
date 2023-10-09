resposta = float(input("Digite uma nota entre zero e dez:"))

while 0 > resposta > 10:
    print("Valor inválido")
    resposta = float(input("Digite uma nota entre zero e dez:"))
    