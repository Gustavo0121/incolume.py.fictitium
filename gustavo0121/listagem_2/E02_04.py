def linha(nome):
    """Mostra as letras do nome uma por linha."""
    vazio = ""
    for i in nome:
        vazio += i
        print(vazio.upper())
    
nome = input("Digite seu nome:")
linha(nome)
