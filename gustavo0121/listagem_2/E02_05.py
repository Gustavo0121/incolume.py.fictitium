def linha(nome):
    """Decomponhe o nome por linha."""
    default1 = ""
    default2 = ""
    for letra in nome:
        default1 += letra
    for i in range(len(nome)):
        default2 = default1[:len(nome) -i:]
        print(default2.upper)
    
nome = input("Digite seu nome:")
linha(nome)