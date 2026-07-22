""""
Aqui o conceito de lista é apresentado..

O phyton não tem tipo de variável, entào basta associar o nome ao seu respectivo valor, como abaixo, a lista NUMS contem os valores 1, 2 e 3, e logo depois printando o seu tipo, <list>
"""
nums = [1,2,3]
print(type(nums))
"""
Aqui adicionamos o valor ao final da lista com o .append na lista.

"""
nums.append(3)
nums.append(4)
nums.append(500)
"""
print(len(nums))) serve para mostrar o tamanho da lista, função base do Phyton
"""
print(len(nums))
"""
Troca de valor através do indice, duas maneiras.
"""
nums[3] = 100
nums.insert(0,-200)
"""
print(nums[posicao]) serve para mostrar o valor contido nessa posicao da lista.
obs: quando é negativo, vai de tras pra frente, pega pelo ultimo.
"""

print(2 in nums)
print(nums[6])
print(nums[-1])
print(nums[-2])
print(nums)