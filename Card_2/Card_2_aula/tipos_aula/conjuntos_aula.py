#print({1, 2, 3})
print(type({1, 2, 3}))
""" conjuntos nao aceitam duplicados, nem printam por referencia a posição """

conj = ({1, 2, 3, 3, 3, 3, 3})
print(conj)