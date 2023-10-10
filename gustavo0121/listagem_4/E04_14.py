tabuada = int(input("Digite um número para ver a tabuada:"))
comeco = int(input("Digite o começo da tabuada:"))
final = int(input("Digite o final da tabuada:"))

while comeco >= final:
        print("O começo tem que ser menor que o final:")
        comeco = int(input("Digite o começo da tabuada:"))
        final = int(input("Digite o final da tabuada:"))
    
while comeco <= final:
    resultado = tabuada * comeco
    print(f"{tabuada} X {comeco} = {resultado}")
    comeco += 1
