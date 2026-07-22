# PEP - proposta de melhoria no phyton.

# def soma(*nums):
#     print (type(nums))
#funcao com numero no main
def soma(*nums):
    total = 0
    for n in nums:
        total += n
    return total
#funcao so com retorno - melhor que o print - empacotada.
def resultado_final(**kwargs):
    # print(type(kwargs))
    status = 'aprovaodo(a)' if kwargs['nota'] >= 7 else 'reprovado(a)'
    return f'{kwargs["nome"]} foi {status} '
