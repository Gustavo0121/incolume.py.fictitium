preco = float(input("Digite o valor do pão:"))
tabela = 0
print(f"Preço do pão: R$ {preco: .2f}")
print("Panificadora Pão de Ontem - Tabela de preços")

for i in range(1,51):
    tabela = i * preco
    print(f"{i} - R$ {tabela: .2f}")
    
