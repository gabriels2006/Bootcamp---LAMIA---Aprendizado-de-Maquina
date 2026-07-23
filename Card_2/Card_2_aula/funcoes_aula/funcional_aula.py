def soma(a, b):
    return a + b

def sub(a, b):
    return a - b


#funcao dentro de funcao
somar = soma
print(somar(3,4))

def operacao_aritmetica(fn, op1, op2):
    return fn(op1, op2)
#funcoes com parametro de outras funcoes, quase como um encapsulamento pelo que entendi.
resultado = operacao_aritmetica(soma, 13, 48)
print(resultado)

resultado = operacao_aritmetica(sub, 13, 48)
print(resultado)

#Aqui o que aparece é o resultado de uma funcao, nao de a+b(é mas não é kkk)
#Otimiza o tempo, somando parcialmente, ele pega partes e junta, como dividir para ganhar, diferente de mandar um resultado final geral.
def soma_parcial(a):
    def concluir_soma(b):
        return a + b
    return concluir_soma

soma_1 = soma_parcial(1)
r1 = soma_1(2)
r2 = soma_1(3)
r3 = soma_1(4)

resultado_final = soma_parcial(10)(12)
print(resultado_final, r1, r2, r3)