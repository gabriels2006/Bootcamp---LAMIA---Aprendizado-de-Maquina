""" O que muda da Tupla para a lista é os parentêses """

nomes = ('Ana', 'Bia', 'Gui', 'Leo', 'Ana')

""" função print - imprimir e verifica se a Bia esta nessa tupla """
print('Bia' in nomes)

""" função print na posicao """
print(nomes[0])

""" função print mas com range de impressao, (de : até) """
print(nomes[1:3])
print(nomes[1:-1])
print(nomes[2:])
print(nomes[:-2])

"""
Se tem virgula, vira tupla!
x = ('Bia',)
print(type(x))

"""
print(len(nomes))
print(type(nomes))
print(nomes)
