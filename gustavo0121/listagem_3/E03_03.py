nome = str(input("Digite seu nome:"))
while len(nome) < 3:
    print("Nome tem que ser maior que 3 caracteres")
    nome = str(input("Digite seu nome:"))


idade = int(input("Digite sua idade:"))
while idade > 150:
    print("Idade tem que ser entre 0 e 150")
    idade = int(input("Digite sua idade"))


salario = float(input("Digite seu salário:"))
while salario < 0:
    print("Salário tem que ser maior que 0")
    salario = float(input("Digite seu salário:"))


sexo = str(input("Digite seu sexo (F - Feminino, M - Masculino)"))
while sexo.upper() != 'F' and sexo.upper() != 'M':
    print("Sexo tem que ser (F ou M)")
    sexo = str(input("Digite seu sexo (F - Feminino, M - Masculino)"))


estado_civil = str(input("Digite seu estado civil (S - solteiro, C - casado, V - viúvo, D - divorciado)"))
while estado_civil.upper() != 'S' and estado_civil.upper() != 'C' and estado_civil.upper() != 'V' and estado_civil.upper() != 'D':
    print("Estado civil tem que ser(S, C, V ou D)")
    estado_civil = str(input("Digite seu estado civil (S - solteiro, C - casado, V - viúvo, D - divorciado)"))
    

    

    