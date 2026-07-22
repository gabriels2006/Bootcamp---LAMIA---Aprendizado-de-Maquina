class Contador:
    contador = 0 #Atributo de classe

    def inst(self):
        return 'Estou bem!'

    def inc_maluco(self):
        self.contador += 1 #Atributo contador local, diferente do inc, todos puxam do contador = 0 no inicio, pode dar erros caso vá tentar incrementar depois de usar esse metodo.
        return self.contador

    @classmethod
    def inc(cls):
        cls.contador += 1
        return cls.contador

    @classmethod
    def dec(cls):
        cls.contador -= 1
        return cls.contador

    @staticmethod     #Caso nao precise acessar nada do que pertence a classe - Nao precisa de instancia
    def mais_um(n):
        return n + 1

c1 = Contador()
print(c1.inc_maluco())
print(c1.inc_maluco())
print(c1.inc_maluco())
print(c1.inc_maluco())


#A partir de uma instacia, o metodo de classe pode ser acessado, porque necessariamente precisa da instancia pra acessar os membros da classe

# print(c1.inc())
# print(c1.inc())
# print(c1.inc())
# print(c1.dec())
# print(c1.dec())
# print(c1.dec())
#
#Outra forma é acessar o metodo direto.
# print(Contador.inc())
# print(Contador.inc())
# print(Contador.inc())
# print(Contador.dec())
# print(Contador.dec())
# print(Contador.dec())
# print(Contador.mais_um(99))

