pessoas = int(input("Quantas pessoas deseja informar a idade:"))
soma = 0

for i in range(pessoas):
    idade = int(input("Digite a sua idade:"))
    soma += idade

media = soma / pessoas
if media <= 25:
    print("A turma é jovem conforme a média calculada")
elif media <= 60:
    print("A turma é adulta conforme a média calculada")
elif media > 60:
    print("A turma é idosa conforme a média calculada")
