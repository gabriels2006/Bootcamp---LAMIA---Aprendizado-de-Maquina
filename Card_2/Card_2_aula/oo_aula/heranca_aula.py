class Carro:
    def __init__(self):
        self.__velocidade = 0

    @property
    def velocidade(self):
        return self.__velocidade

    def acelerar(self):
        self.__velocidade += 5
        return self.__velocidade

    def frear(self):
        self.__velocidade -= 5
        return self.__velocidade

class Uno(Carro):
    pass

#A heranca aqui é vista, pois Ferrari puxa os dados de Carro, e então sobreescreve
class Ferrari(Carro):
    def acelerar(self):
        super().acelerar() #Super reecreve a funcao anterior, nesse caso, chama de novo, acelerando 2 vezes.
        return super().acelerar()


#c1 = Uno()
c1 = Ferrari()
print(c1.acelerar())
print(c1.acelerar())
print(c1.acelerar())
print(c1.frear())
print(c1.frear())
print(c1.frear())