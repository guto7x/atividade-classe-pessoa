# AULA 11 - 12

# from datetime import date

# class Pessoa():
#     def __init__(self, nome, nascimento="00/00/0000", cpf=None, rg=None, endereco=None, estado_civil=None):
#         self.__nome = nome
#         self.__nascimento = nascimento
#         self.__cpf = cpf
#         self.__rg = rg
#         self.__endereco = endereco
#         self.__estado_civil = estado_civil
#         self.__idade = self.__calcular_idade()
    
#     def get_nome(self):
#         return self.__nome

#     def set_nome(self, nome):
#         self.__nome = nome

#     def get_nascimento(self):
#         return self.__nascimento

#     def set_nascimento(self, nascimento):
#         self.__nascimento = nascimento
#         self.__idade = self.__calcular_idade()  

#     def get_cpf(self):
#         return self.__cpf

#     def set_cpf(self, cpf):
#         self.__cpf = cpf

#     def get_rg(self):
#         return self.__rg

#     def set_rg(self, rg):
#         self.__rg = rg

#     def get_endereco(self):
#         return self.__endereco

#     def set_endereco(self, endereco):
#         self.__endereco = endereco

#     def get_estado_civil(self):
#         return self.__estado_civil

#     def set_estado_civil(self, estado_civil):
#         self.__estado_civil = estado_civil

#     def get_idade(self):
#         return self.__idade

#     def dados(self):
#         return f'Nome: {self.get_nome()}\nNascimento: {self.get_nascimento()}\nCPF: {self.get_cpf()}\nRG: {self.get_rg()}\nEndereço: {self.get_endereco()}\nEstado Civil: {self.get_estado_civil()}\nIdade: {self.get_idade()} anos'

#     def __calcular_idade(self):
#         hoje = date.today()
#         nascimento_formatado = self.get_nascimento().split('/')
#         dia_nascimento = int(nascimento_formatado[0])
#         mes_nascimento = int(nascimento_formatado[1])
#         ano_nascimento = int(nascimento_formatado[2])

#         idade_calculada = hoje.year - ano_nascimento - ((hoje.month, hoje.day) < (mes_nascimento, dia_nascimento))

#         return idade_calculada

# pessoa = Pessoa(nome="Gustavo", nascimento="16/07/2006", cpf="718.027.761-41", rg="n sei", endereco="Buriti Sereno, Rua Campo Belo, Q37 - L39, Aparecida de Goiânia - Goiás", estado_civil="Solteiro")
# print(pessoa.dados())

#
# @Property
#

from datetime import date

class Pessoa():
    def __init__(self, nome, nascimento="00/00/0000", cpf=None, rg=None, endereco=None, estado_civil=None):
        self.__nome = nome
        self.__nascimento = nascimento
        self.__cpf = cpf
        self.__rg = rg
        self.__endereco = endereco
        self.__estado_civil = estado_civil
        self.__idade = self.__calcular_idade()

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def nascimento(self):
        return self.__nascimento

    @nascimento.setter
    def nascimento(self, nova_data):
        self.__nascimento = nova_data
        self.__idade = self.__calcular_idade()

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, novo_cpf):
        self.__cpf = novo_cpf

    @property
    def rg(self):
        return self.__rg

    @rg.setter
    def rg(self, novo_rg):
        self.__rg = novo_rg

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, novo_endereco):
        self.__endereco = novo_endereco

    @property
    def estado_civil(self):
        return self.__estado_civil

    @estado_civil.setter
    def estado_civil(self, novo_estado_civil):
        self.__estado_civil = novo_estado_civil

    @property
    def idade(self):
        return self.__idade

    def dados(self):
        return f'Nome: {self.nome}\nNascimento: {self.nascimento}\nCPF: {self.cpf}\nRG: {self.rg}\nEndereço: {self.endereco}\nEstado Civil: {self.estado_civil}\nIdade: {self.idade} anos'

    def __calcular_idade(self):
        hoje = date.today()
        nascimento_formatado = self.nascimento.split('/')
        dia_nascimento = int(nascimento_formatado[0])
        mes_nascimento = int(nascimento_formatado[1])
        ano_nascimento = int(nascimento_formatado[2])

        idade_calculada = hoje.year - ano_nascimento - ((hoje.month, hoje.day) < (mes_nascimento, dia_nascimento))

        return idade_calculada

pessoa = Pessoa(nome="Gustavo", nascimento="16/07/2006", cpf="718.027.761-41", rg="n sei", endereco="Buriti Sereno, Rua Campo Belo, Q37 - L39, Aparecida de Goiânia - Goiás", estado_civil="Solteiro")
print(pessoa.dados())