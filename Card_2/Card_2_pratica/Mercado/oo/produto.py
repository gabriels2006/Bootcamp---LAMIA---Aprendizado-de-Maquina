# Classe Produto - os métodos são privados
class Produto:
    def __init__(self, nome, preco=1.99, quantidade=0):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def __str__(self):
        return f"{self.nome} - R$ {self.preco:.2f} (Qtd: {self.quantidade})"

    def atualizar_quantidade(self, qtd):
        self.quantidade += qtd

    def aplicar_desconto(self, percentual):
        self.preco *= (1 - percentual/100)