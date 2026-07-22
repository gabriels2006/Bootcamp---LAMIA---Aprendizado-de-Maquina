#!phyton 3
""" função print - imprimir """

# print('Bem vindo')
""" função import - importa outro arquivo, pasta para ser usado nesse arquivo """

""" função print - imprimir, mas nesse caso, imprime o nome do arquivo/modulo """
#print(__name__)
""" função print - imprimir, mas nesse caso, imprime o nome do package/pacote """
#print(__package__)

"""
Basicos
"""
#import pacote.sub.arquivo
#from tipos import variaveis, basicos

"""
Tipos
"""
#import tipos.variaveis
#import tipos.lista
#import tipos.tuplas
#import tipos.conjuntos
#import tipos.dicionario

"""
Operadores
"""
#import operadores.unarios
#import operadores.aritimeticos
#import operadores.relacionais
#import operadores.atribuicao
#import operadores.logicos
#import operadores.ternario


"""
Controle
"""
#import controle.if_1
#import controle.if_2
#import controle.for_1
#import controle.while_1
#import controle.outros_exemplos

"""
Funcoes
"""

# from funcoes import basico
#
# basico.saudacao('Maria')
# basico.saudacao('Joao', 33)
# basico.saudacao(idade= 89)
# basico.saudacao()
# #A ordem dos parametros pode ser alterada, desde que se saiba os parametros e coloque seu respectivo valor@!
# a = basico.soma_e_multi(x=10, a=2, b=3)
# b = basico.soma_e_multi(x=20, a=3, b=7)
# resultado = a + b
# print(resultado)
#
# from funcoes import args
#
# # args.soma(1)
# # args.soma(1, 2, 3)
# # args.soma()
#
# s = args.soma(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(s)
#
# resultado = args.resultado_final(nome= 'Pedro', nota=6.3)
# print(resultado)
#
# from funcoes import funcional
import funcoes.map_reduce
import funcoes.lambdas
import funcoes.comprehension

import oo.produto
import oo.heranca
import oo.membros