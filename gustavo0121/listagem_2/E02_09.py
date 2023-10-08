def valid_cpf(cpf):
    """Valida o formato do digitado do CPF"""
    while cpf[3] != '.' or cpf[7] != '.' or cpf[11] != '-':
        print('CPF digitado incorretamente.')
        break
    
    print('CPF digitado corretamente.')

cpf = str(input('Digite o CPF no seguinte formato: [xxx.xxx.xxx-xx]: '))
valid_cpf(cpf)