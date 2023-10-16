print(
    "Qual o melhor Sistema Operacional para uso em servidores?\n"
"1- Windows Server\n"
"2- Unix\n"
"3- Linux\n"
"4- Netware\n"
"5- Mac OS\n"
"6- Outro\n"
)

indice_ganhador_percent =[]
indice_ganhador = []
votos_sistema = []
sistemas = ['Windows Server','Unix','Linux','Netware','Mac OS','Outro']

while True:
    voto = int(input("Digite o seu voto (1 a 6) ou 0 para encerrar:"))

    if voto < 0 or voto > 6:
        print("O número tem que ser entre 1 e 23")
        continue
    if voto == 0:
        break

    votos_sistema.append(voto)


print('Sistema Operacional','\t', 'Votos','\t','%')
print('-'*19,'\t','-'*5,'\t','-'*3)

contador = 0
for i in range(len(sistemas)):
    porcentagem_voto = round((votos_sistema.count(contador+1) / len(votos_sistema)) * 100)
    print('{:<19}{:>10}{:>5}%'.format(sistemas[contador],votos_sistema.count(contador+1),porcentagem_voto))
    contador +=1
    indice_ganhador.append(votos_sistema.count(contador+1))
    indice_ganhador_percent.append(porcentagem_voto)

print('{:<19}{:>10}'.format('-'*19,'-'*5,))
print('{:<19}{:>10}'.format('Total',len(votos_sistema)))

vitoria = max(indice_ganhador)

for i in range(len(sistemas)):
    if indice_ganhador[i] == vitoria:
        print(f"O sistema mais votado foi o {sistemas[i]} com {max(indice_ganhador)} votos correspondendo a {max(indice_ganhador_percent)} % dos votos.")
