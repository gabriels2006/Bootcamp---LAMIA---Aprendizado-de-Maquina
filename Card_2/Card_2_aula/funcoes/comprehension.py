from functools import reduce

alunos = [
    {'nome': 'Ana', 'nota': 7.2},
    {'nome': 'Breno', 'nota': 8.1},
    {'nome': 'Claudia', 'nota': 8.7},
    {'nome': 'Pedro', 'nota': 6.4},
    {'nome': 'Rafael', 'nota': 6.7},
]

obter_nota = lambda aluno: aluno['nota']
somar = lambda a, b: a + b

#Aqui é outra forma de obter o mesmo resultado do lambda, entretanto menor e com uma lógica mais direta
#O que acontece é, gerar um laço de repetição percorrendo o dicionário, depois capta apenas as notas.
alunos_aprovados = [aluno for aluno in alunos if aluno['nota'] >= 7]
notas_alunos_aprovados = [aluno['nota']for aluno in alunos_aprovados]

#usa o reduce para sintetizar e unir os resultados das funções e printa no console.
total = reduce(somar, notas_alunos_aprovados)

print(total / len(alunos_aprovados))
