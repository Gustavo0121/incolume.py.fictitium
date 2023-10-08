def tam_string(string1, string2):
    """compara o conteúdo e o tamanho de duas strings"""
    tamanho1 = len(string1)
    tamanho2 = len(string2)
    print(f"String 1: {string1}\nString 2: {string2}")
    print(f"Tamanho de {string1}: {tamanho1} carac.\nTamanho de {string2}: {tamanho2} carac.")

    if tamanho1 != tamanho2:
        print("As duas strings são de tamanho diferente")
    else:
        print("As duas strings são do mesmo tamanho")

    if string1 != string2:
        print("As duas strings possuem conteúdo diferente.")
    else:
        print("As duas string possuem o mesmo conteúdo")
    
string1 = input("Digite algo:")
string2 = input("Digite outra coisa:")
tam_string(string1, string2)