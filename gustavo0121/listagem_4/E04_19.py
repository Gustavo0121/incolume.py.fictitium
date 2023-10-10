valor_divida = float(input("Digite o valor da dívida:"))
parcelas = 1
juros = 0
print("|Valor da Dívida|Valor dos Juros|Quantidade de Parcelas|Valor da Parcela|")
while parcelas <= 12:
    juros = (5 / 3) * parcelas + 5
    if parcelas == 1:
        juros = 0

    valor_do_juros = valor_divida * (juros / 100)
    valor_total = valor_divida + valor_do_juros
    valor_da_parcela = valor_total / parcelas
    print(f"|R$ {valor_total:.2f}\t|R$ {valor_do_juros:.2f}\t|{parcelas}\t\t\t|R$ {valor_da_parcela:.2f}")
    if parcelas == 1:
        parcelas -= 1
    parcelas += 3
    