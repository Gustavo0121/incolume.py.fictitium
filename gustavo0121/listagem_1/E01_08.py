def salario(din_horas, horas_trab):
    """Calcula o salário a partir das horas trabalhadas."""
    salario = din_horas * horas_trab
    print(f"O salário é de {salario: 0.2f} R$")


din_horas = float(input("Digite o quanto ganha por hora:"))
horas_trab = float(input("Digite a quantidade de horas trabalhadas no mês:"))

salario(din_horas, horas_trab)