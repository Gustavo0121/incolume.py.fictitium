idade = []
altura = []

for i in range(5):
    print(f"Pessoa {i + 1}")
    idade.append(int(input("Digite sua idade:")))
    altura.append(int(input("Digite sua altura:")))

print(f"As idades são: {idade[::-1]} e as alturas são {altura[::-1]}")