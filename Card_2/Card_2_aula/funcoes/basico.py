#Toda funcao é um modulo, nesse caso, por padrao a funçào no phyton é definida por def e dentro vai o bloco de código
# def saudacao():
#     print('Bom dia!')

#As funcoes podem ser escritas com o mesmo nome, e assim serem sobreescritas, de maneira que pode ser chamada com ou sem os parametros
# def saudacao():
    # print(f'Boa tarde!')

#Abaixo temos o tipo de saudacao padrão, isso significa que pode ser colocado um padrão para todas as funções, uma espécie de resposta quando tudo ficar em braco
def saudacao(nome = 'Pessoa', idade = 20):
    print(f'Bom dia {nome}! Você nem parece ter {idade} anos!')
#nome do modulo

def soma_e_multi(a, b, x):
    return a + b * x

#Essa funcao serve como um main dentro do java, em cada funcao. Ele só roda se o arquivo principal e inicial for esse, se não, roda os outros módulos..
if __name__ == '__main__':
    saudacao('Ana', idade = 30)

