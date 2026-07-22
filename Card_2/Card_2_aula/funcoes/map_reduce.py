from functools import reduce
from struct import calcsize


def somar_nota(delta):
    def calc(nota):
        return nota + delta
    return calc

def mais_um_meio(nota):
    return nota + 1.5

#o map serve para transformar uma lista em qualquer outra coisa, mapeada.
notas = [6.4, 7.2, 5.8, 8.4]
notas_finais_1 = map(somar_nota(1.5), notas)
notas_finais_2 = map(somar_nota(1.6), notas)

#*****O codigo da aula estava exatamente assim, porem na versao do phyton 3, precisa do list para esse print
#print(notas_finais)
print(list(notas_finais_1))
print(list(notas_finais_2))

# total = 0 Metodo padrão
# for n in notas:
#     total += n
# print(total)

#usando reduce - Ele literalmente reduz o tamanho do codigo para uma linha, basta a funcao, referencia e valor inicial, acabou.

def somar(a, b):
    return a + b

total = reduce(somar, notas, 0)
print(total)




#Metodo padrao
# for i, nota in enumerate(notas):
#     notas[i] = nota + 1.5
#
# for i in range(len(notas)):
#     notas[i] = notas[i] + 1.5