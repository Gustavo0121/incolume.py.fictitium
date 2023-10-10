produto = float(input("Informe o preço do produto ou digite 0 para encerrar a compra:"))
soma = 0
contador = 1 
dinheiro= 0
troco = 0

print("Lojas Tabajara ")
while True:
    if produto == 0:
        break
        
    soma += produto
    produto = float(input("Informe o preço do produto ou digite 0 para encerrar a compra:"))
    print(f"Produto {contador}: R$ {produto}")
    contador += 1 
    

dinheiro = float(input("Quanto de dinheiro irá dar:"))
if dinheiro > soma:
    troco = dinheiro - soma
else:
        print("Dinheiro insuficiente!")
    
    
print(f"Total: R$ {soma}")
print(f"Dinheiro: R$ {dinheiro}")
print(f"Troco: R$ {troco}")