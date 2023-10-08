def linha(nome):
    """Mostra as letras do nome uma por linha."""
    for i in nome:
        print(i.upper())
    
nome = input("Digite seu nome:")
linha(nome)
