#while, repeticao sem saber quantas vezes sera necessario.

# x = 0
#
# while x != -1:
#     x = float(input('Informe um numero ou -1 para sair: '))
#
# print('Fim!')

#programa basico para media de uma turma
total = 0
qtde = 0
nota = 0

while nota != -1:
    nota = float(input('Informe a nota ou -1 para sair: '))
    if nota != -1:
        qtde += 1
        total += nota

print(f'A média da turma é {total / qtde}')
print('Fim!')

# x = 10
#
# while x:
#     print(x)
#     x -= 1
# print('Fim!')