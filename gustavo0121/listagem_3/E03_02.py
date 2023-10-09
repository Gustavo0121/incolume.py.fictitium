usuario = str(input("Digite seu usuário:"))
senha = str(input("Digite sua senha:"))

while usuario == senha:
    print("Usuário e senha não podem ser iguais")
    usuario = str(input("Digite seu usuário:"))
    senha = str(input("Digite sua senha:"))