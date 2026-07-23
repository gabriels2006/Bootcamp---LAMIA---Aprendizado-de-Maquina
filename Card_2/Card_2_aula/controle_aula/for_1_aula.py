#Para gerar um laço de reptição, ele roda através do range, tamanho.
#Laco base, sem o ultimo
for i in range(10):
  print(i, end=' ')

print('')

#laco de 1 até 11, sem o ultimo.
for i in range(1, 11):
   print(i, end=' ')

print('')

#laco de 20 até 0, com o passo -3
for i in range(20, 0, -3):
   print(i, end=' ')

print('')

#Aqui percorre uma lista, e no fim de cada posicao, adiciona o espaco em branco
nums = [2,4,6,8]

for n in nums:
    print(n, end=' ')

print('')
#Aqui percorre uma string, e no fim de cada posicao, adiciona o espaco em branco, mantendo na linha
texto = 'Python é muito massa'

for letra in texto:
    print(letra, end=' ')

print('')
#Aqui percorre uma definicao/conjunto
for n in {1, 2, 3, 4, 4, 4}:
    print(n, end=' ')

print('')
#Aqui percorre um dicionario
produto = {
    'nome': 'Caneta',
    'preco': 8.80,
    'desc': 0.5
}
#Aqui percorre pega o atibuto e mosta todos os seus componentes
for atrib in produto:
    print(atrib, '==>', produto[atrib], end=' ')

print('')
#Aqui percorre pega o atibuto e mosta todos os seus componentes
for atrib, valor in produto.items():
    print(atrib, '=>', valor, end=' ')

print('')
#Aqui percorre pega o atibuto e mosta todos os seus componentes/valores
for valor in produto.values():
    print(valor, end=' ')

print('')
#Aqui percorre pega o atibuto e mosta apenas as raizes de seus componentes
for atrib in produto.keys():
    print(atrib, end=' ')