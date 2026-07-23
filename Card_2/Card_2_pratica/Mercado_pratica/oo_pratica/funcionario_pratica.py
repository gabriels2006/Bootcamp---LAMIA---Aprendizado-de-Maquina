from Card_2.Card_2_pratica.Mercado_pratica.oo_pratica.pessoa_pratica import Pessoa #Usando conceito de importacao - Heranca

# Funcionário herda de Pessoa
class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, salario):
        super().__init__(nome, idade) #Utilizado para poder reescrever o nome e idade direto por aqui
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return f"{self.nome} - {self.cargo} (R$ {self.salario:.2f})"