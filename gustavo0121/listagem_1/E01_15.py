def salario(din_horas, horas_trab):
    """Calcula o salário bruto a partir das horas trabalhadas, o INSS, o sindicato e o salário líquido."""
    salario_bruto = din_horas * horas_trab
    inss = (8 * salario_bruto) / 100
    sindicato = (5 * salario_bruto) / 100
    salario_liquido = salario_bruto - inss - sindicato

    print(f"O salário bruto é de: {salario_bruto: 0.2f}R$")
    print(f"Você pagou ao INSS: {inss: 0.2f}R$")
    print(f"Você pagou ao sindicato: {sindicato: 0.2f}R$")
    print(f"O salário líquido é de: {salario_liquido: 0.2f}R$")


din_horas = float(input("Digite o quanto ganha por hora:"))
horas_trab = float(input("Digite a quantidade de horas trabalhadas no mês:"))

salario(din_horas, horas_trab)
