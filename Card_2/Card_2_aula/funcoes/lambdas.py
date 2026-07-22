from functools import reduce

alunos = [
    {'nome': 'Ana', 'nota': 7.2},
    {'nome': 'Breno', 'nota': 8.1},
    {'nome': 'Claudia', 'nota': 8.7},
    {'nome': 'Pedro', 'nota': 6.4},
    {'nome': 'Rafael', 'nota': 6.7},
]
#funcao para definir em uma unica linha - Normalmente "Sem nome" - anonima, serve para ser um quebra galho caso vá utilizar uma unica vez....
aluno_aprovado = lambda aluno: aluno['nota'] >= 7
# aluno_honra = lambda aluno: aluno['nota'] >= 9
obter_nota = lambda aluno: aluno['nota']
somar = lambda a, b: a + b

#O filter serve literalmente para filtrar, usando assim a função lambda como base anterior para esse refinamento.
alunos_aprovados1 = filter(aluno_aprovado, alunos)
#aqui coloquei outra função pois no phyton2 funcionava como acima, mas no 3 precisa converter o filter para uma lista, de maneira explicita
alunos_aprovados2 = list(filter(aluno_aprovado, alunos))
#Aqui o map transforma a lista em um float.
notas_alunos_aprovados = map(obter_nota, alunos_aprovados1)
total = reduce(somar, notas_alunos_aprovados, 0)

print(total / len(alunos_aprovados2))
# print(obter_nota(alunos[2]))
# print(list(alunos_aprovado))
#novamente o list... Apenas para mostrar no console.
# print(list(notas_alunos_aprovados))