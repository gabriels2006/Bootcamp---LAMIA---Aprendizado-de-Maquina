from oo.produto import Produto #Conceito de heranca

# Classe Estoque
class Estoque:
    def __init__(self):
        self.produtos = []
#Metodos basicos para um mercado
    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def listar_produtos(self):
        for p in self.produtos:
            print(p)

    def buscar_produto(self, nome):
        return next((p for p in self.produtos if p.nome.lower() == nome.lower()), None)
#filtro para produtos - list filter pois estamos no phyton3! :)
    def produtos_caros(self, limite=100):
        return list(filter(lambda p: p.preco > limite, self.produtos))
