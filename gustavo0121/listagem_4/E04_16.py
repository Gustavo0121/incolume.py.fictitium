ano_comeco = 1995
salario = 1000
ano_final = int(input("Digite o último ano do contrato: "))
ajuste = 0.15
ano_comeco = ano_comeco + 1
contador = 1

while (ano_comeco <= ano_final):
    if (ano_comeco <= 1995 or contador  == 1):
        ajuste = ajuste
    else:
        ajuste = ajuste * 2
    salario = salario + (salario * ajuste)
    print(f"Ajuste de:{ano_comeco} {ajuste*10: .1f} %")
    print(f"Salário ajustado:{salario: .2f}")
    ano_comeco +=  1