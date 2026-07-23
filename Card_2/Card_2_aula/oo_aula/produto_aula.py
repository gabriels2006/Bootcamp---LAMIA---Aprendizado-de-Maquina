
#Nada no phyton é implicito por isso a classe normalmente comeca com Self, ela se autoreferencia, depois vem os parametros, assim como no Java.
#Tudo vai dentro de uma funcao __init__ para inicializar e tornar existente a classe - Seria o método construtor
class Produto:
    def __init__(self, nome, preco = 1.99, desc = 0):
        self.nome = nome #privado
        self.__preco = preco
        self.desc = desc
        #esta instaciado no mesmo lugar, nao precisa passar como referencia

    #Funcionam basicamente como os getters e setters, melhorando o encapsulamento.
    @property
    def preco(self):
        return f'R$ {self.__preco:.2f}'
    #Metodo
    @preco.setter
    def preco(self, novo_preco):
        if novo_preco > 0:
            self.__preco = novo_preco

    @property #Transforma um método em uma variavel/atributo
    def preco_final(self):
        return (1 - self.desc) * self.__preco

    # @property #torna o privado visivel -
    # def nome(self):
    #     return self.nome

p1 = Produto('Caneta', 10, 0.1)
p2 = Produto('Caderno', 14, 0.5)

p1.preco = 70.89
p2.preco = 17.99

print(p1.nome, p1.preco, p1.desc, p1.preco_final)
print(p2.nome, p2.preco, p2.desc, p2.preco_final)