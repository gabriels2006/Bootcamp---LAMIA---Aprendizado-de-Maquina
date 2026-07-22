a = 'valor' #True
#tipos que existem ou nao, condicional simples. Se possui valor ou espaco, existe! Ja que conta com caractere....
#print(not 'valor')
a = 0 #False
a = -0.001 #True
a = '' #False
a = ' ' #True
a = [] #False
a = {} #False

if a:
    print('Existe!!!')
else:
    print('não existe ou zero ou vazio...')