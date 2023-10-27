class Bola:
    def __init__(self, cor: str, circunferencia: float, material: str):
        """Construtor."""
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    
    def trocar_cor(self, cor_nova):
        """Trocar cor."""
        self.cor = cor_nova

    
    def mostrar_cor(self):
        """Mostrar cor."""
        print(self.cor)


class Quadrado:
    def __init__(self, tamanho_lado):
        """Construtor."""
        self.tamanho_lado = tamanho_lado

    
    def mudar_valor_lado(self, novo_tamanho_lado):
        """Mudar tamanho do lado."""
        self.tamanho_lado = novo_tamanho_lado

    
    def retornar_valor_lado(self,):
        """Retornar tamanho do lado."""
        return (self.tamanho_lado)

    
    def calcular_valor_area(self, tamanho_lado):
        """Calcular valor da área."""
        area = tamanho_lado ** 2
        return (area)


class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        """Construtor."""
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    
    def envelhecer(self, idade):
        """Envelhecer a idade em ano."""
        idade += 1
        return idade

    
    def engordar(self, peso):
        """Engordar um quilo."""
        peso += 1
        return peso

    
    def emagrecer(self, peso):
        """Emagrecer um quilo."""
        peso -= 1
        return peso

    
    def crescer(self, idade, altura):
        """Crescer de acordo com sua idade"""
        if idade < 21:
            altura += 0.05
        else:
            altura += 0.01
        return altura


class Conta_corrente:
    def __init__(self, numero_conta, nome_correntista, saldo: float = 0):
        """Construtor."""
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    
    def alterar_nome(self, nome_novo):
        """Alterar o nome."""
        self.nome_correntista = nome_novo
        return self.nome_correntista

    
    def depositar(self, valor):
        """Depositar um valor."""
        self.saldo += valor
        return self.saldo

    
    def sacar(self, valor):
        """Sacar um valor."""
        self.saldo -= valor
        return self.saldo


class Tv:
    def __init__(self, canal, volume):
        """Construtor."""
        self.canal = canal
        self.volume = volume

    
    def aumentar_volume(self,):
        """Aumentar o volume."""
        if self.volume <= 99:
            self.volume += 1
        else:
            raise ValueError('Volume não pode ser maior que 100.')
        return self.volume

    
    def abaixar_volume(self,):
        """Abaixar o volume."""
        if self.volume >= 1:
            self.volume -= 1
        else:
            raise ValueError('Volume não pode ser menor que 0.')
        return self.volume

    
    def trocar_canal(self, novo_canal):
        """Trocar de canal."""
        if 0 < novo_canal < 1000:
            self.canal = novo_canal
        else:
            raise ValueError('Canal tem que ser entre 0 e 1000.')
        return self.canal


class Tamagushi:
    def __init__(self, nome: str, fome: str, saude: str, idade: int):
        """Construtor."""
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alterar_nome(self, nome_novo):
        """Alterar nome."""
        self.nome = nome_novo

    def retornar_nome(self,):
        """Retornar nome."""
        return self.nome  

    def alterar_fome(self, fome_nova):
        """Alterar fome."""
        self.fome = fome_nova

    def retornar_fome(self,):
        """Retornar fome."""
        return self.fome

    def alterar_saude(self, saude_nova):
        """Alterar saúde."""
        self.saude = saude_nova

    def retornar_saude(self,):
        """Retornar saúde."""
        return self.saude

    def alterar_idade(self, idade_nova):
        """Alterar idade."""
        self.idade = idade_nova

    def retornar_idade(self,):
        """Retornar idade."""
        return self.idade

    def calcular_humor(self, fome, saude):
        """Calcular humor."""
        humor = 'Humor estável'
        if fome == 'alta' and saude == 'baixa':
            humor = 'Mal-humorado'
        if fome == 'baixa' and saude == 'alta':
            humor = 'Bem-humorado'
        return humor


class Macaco:
    def __init__(self, nome: str, bucho: str = ''):
        """Construtor."""
        self.nome = nome
        self.bucho = bucho

    def comer(self, alimento):
        """Comer."""
        self.bucho += alimento + ' '

    def diregir(self,):
        """Digerir"""
        self.bucho = ''

    def ver_bucho(self,):
        """Ver a comida que está no estômago."""
        return self.bucho


class Bomba_combustivel:

def __init__(self, tipo_combustivel, valor_litro, qtd_combustivel):
    """Construtor."""
    self.tipo_combustivel = tipo_combustivel
    self.valor_litro = valor_litro
    self.qtd_combustivel = qtd_combustivel

def abastecer_por_valor(self, valor):
    """Abastecer combustível pelo valor informado."""
    litros = valor // self.valor_litro
    self.qtd_combustivel -= litros
    return litros

def abastecer_por_litro(self, litro):
    """Abastecer combustível pelo litro informado."""
    self.qtd_combustivel -= litro
    valor = litro * self.valor_litro
    return valor

def alterar_valor(self, valor_novo):
    """Alterar valor do litro da gasolina."""
    self.valor_litro = valor_novo

def alterar_combustivel(self, combustivel_novo):
    """Alterar tipo de combustível."""
    self.tipo_combustivel = combustivel_novo

def alterar_qtd_combustivel(self, qtd_nova):
    """Alterar quantidade de combustível restante na bomba."""
    self.qtd_combustivel = qtd_nova


class Carro:
    def __init__(self, consumo_km_litro, qtd_combustivel_tanque: float = 0):
        """Construtor."""
        self.consumo = consumo_km_litro
        self.combustivel = qtd_combustivel_tanque

    def andar(self, qtd_kilometros):
        """Andar."""
        self.combustivel -= qtd_kilometros // self.consumo

    def adcionar_gasolina(self, qtd_gasolina):
        """Abastecer o carro."""
        self.combustivel += qtd_gasolina

    def obter_gasolina(self,):
        """Retornar a gasolina restante no tanque."""
        return self.combustivel


class Funcionario:
    def __init__(self, nome: str, salario):
        """Construtor."""
        self.nome = nome
        self.salario = salario

    def mostrar_nome(self,):
        """Retorna o nome."""
        return self.nome

    def mostrar_salario(self,):
        """Retorna o salário."""
        return self.salario


class Funcionario:
    def __init__(self, nome: str, salario):
        """Construtor."""
        self.nome = nome
        self.salario = salario

    def aumentar_salario(self, percent):
        """Aumentar o salário de acordo com a porcentagem.."""
        self.salario += self.salario * (percent/100)


    def mostrar_nome(self,):
        """Retorna o nome."""
        return self.nome

    def mostrar_salario(self,):
        """Retorna o salário."""
        return self.salario



Gustavo Ribeiro <gus0512san@gmail.com>
qui., 26 de out., 23:19 (há 11 horas)
para gustavo.ribeiro2018

class Tamagushi:
    def __init__(self, nome: str, fome: int, saude: int, idade: int):
        """Construtor."""
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alterar_nome(self, nome_novo):
        """Alterar nome."""
        self.nome = nome_novo

    def retornar_nome(self,):
        """Retornar nome."""
        return self.nome  

    def alimentar(self, qtd_comida):
        """Alimentar."""
        if qtd_comida >= 3:
            self.fome -= 3
        if qtd_comida == 2:
            self.fome -= 2
        self.fome -= 1

    def retornar_fome(self,):
        """Retornar fome."""
        return self.fome

    def alterar_saude(self, saude_nova):
        """Alterar saúde."""
        self.saude = saude_nova

    def retornar_saude(self,):
        """Retornar saúde."""
        return self.saude

    def alterar_idade(self, idade_nova):
        """Alterar idade."""
        self.idade = idade_nova

    def retornar_idade(self,):
        """"Retornar idade."""
        return self.idade

    def brincar(self, tempo):
        """Brincar."""
        if tempo == 3:
            self.saude += 3
        if tempo == 2:
            self.saude += 2
        self.saude += 1


    def calcular_humor(self, fome, saude):
        """Calcular humor."""
        humor = 'Humor estável'
        if fome >= 3 and saude <= 0:
            humor = 'Mal-humorado'
        if fome <= 0 and saude >= 3:
            humor = 'Bem-humorado'
        return humor