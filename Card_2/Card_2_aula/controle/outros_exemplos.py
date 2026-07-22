pessoas = ['Gui', 'Rebeca']
adjs = ['Sapeca', 'Inteligente']

for p in pessoas:
    for a in adjs:
        print(f'{p} é {a}!')

for i in [1, 2, 3]:
    pass #aqui passa direto pelo codigo, nao muda nada

for i in range(1, 11):
    if i % 2 == 1:
        continue # continua a rodar o codigo enquanto for verdade o bloco
    print(i)

for i in range(1, 11):
    if i == 5:
        break # para/ quebra o bloco quando for verdade.
    print(i)