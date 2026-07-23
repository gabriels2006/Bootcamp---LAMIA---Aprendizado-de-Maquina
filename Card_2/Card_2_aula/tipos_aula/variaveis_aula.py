""" variaveis """
a = 3
b = 4.4

""" operação com variaveis a e b """
print(a+b)

""" variaveis """
texto = 'Sua idade é... '
idade = 23

""" gambiarra de printar variaveis de tipo diferente (Concatenar) """
#print(texto+ str(idade))

""" Concatenar variaveis """
print(f'{texto} {idade}')

""" operação com variavel de texto """
saudacao = 'bom dia '
print(3 * saudacao)

""" Constante e manipulação por fórmula e função POW (potencia) """
PI = 3.14
#input('Informe o raio da circ? ')
raio = float(input('Informe a raio da circ '))
#area = PI * raio * raio
area = PI *pow(raio,2)

""" printa o tipo da variavel """
print(type(raio))
#print(area)

print(f'A area da circ é {area} m2.')
