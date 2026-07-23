#Condicionais simples, representacao com nota do aluno, if - se, elif - else if - ou, else - se não

nota = float(input('Informe a nota do aluno: '))
comportado = True if input('Comportado (y/n): ') == 'y' else False
#Aqui não se separa por chaves ou parenteses as condicionais, o bloco apenas precisa do espaco..

if nota >= 9 and comportado:
    print('Duas palavras: para bens! :P')
    print('Quadro de Honra')
elif nota >= 7:
    print('Aprovado')
elif nota >= 5.5:
    print('Recuperação')
elif nota >= 4.5:
    print('Recuperação + Trabalho')
else:
    print('Reprovado!')

print(nota)