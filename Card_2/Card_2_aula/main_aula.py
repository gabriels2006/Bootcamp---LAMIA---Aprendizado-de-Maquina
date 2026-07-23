#!python 3
""" função print - imprimir """

# print('Bem vindo')
""" função import - importa outro arquivo, pasta para ser usado nesse arquivo """

""" função print - imprimir, mas nesse caso, imprime o nome do arquivo/modulo """
# print(__name__)
""" função print - imprimir, mas nesse caso, imprime o nome do package/pacote """
# print(__package__)

"""
Basicos
"""
#import pacote_aula.sub_aula.arquivo_aula
# from tipos_aula import variaveis_aula, basicos_aula

"""
Tipos
"""
# import tipos_aula.variaveis_aula
# import tipos_aula.lista_aula
# import tipos_aula.tuplas_aula
# import tipos_aula.conjuntos_aula
# import tipos_aula.dicionario_aula

"""
Operadores
"""
# import operadores_aula.unarios_aula
# import operadores_aula.aritmeticos_aula
# import operadores_aula.relacionais_aula
# import operadores_aula.atribuicao_aula
# import operadores_aula.logicos_aula
# import operadores_aula.ternario_aula

"""
Controle
"""
# import controle_aula.if_1_aula
# import controle_aula.if_2_aula
# import controle_aula.for_1_aula
# import controle_aula.while_1_aula
# import controle_aula.outros_exemplos_aula

"""
Funcoes
"""
# from funcoes_aula import basico_aula
#
# basico_aula.saudacao('Maria')
# basico_aula.saudacao('Joao', 33)
# basico_aula.saudacao(idade=89)
# basico_aula.saudacao()
# # A ordem dos parametros pode ser alterada, desde que se saiba os parametros e coloque seu respectivo valor!
# a = basico_aula.soma_e_multi(x=10, a=2, b=3)
# b = basico_aula.soma_e_multi(x=20, a=3, b=7)
# resultado = a + b
# print(resultado)
#
# from funcoes_aula import args_aula
#
# s = args_aula.soma(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(s)
#
# resultado = args_aula.resultado_final(nome='Pedro', nota=6.3)
# print(resultado)
#
# from funcoes_aula import funcional_aula

import funcoes_aula.map_reduce_aula
import funcoes_aula.lambdas_aula
import funcoes_aula.comprehension_aula

import oo_aula.produto_aula
import oo_aula.heranca_aula
import oo_aula.membros_aula
