#lockdown = True
lockdown = False
grana = 30
#condicionais simples, com ternario, assim como no C - Se ou se não com condição.
status = 'Em casa' if lockdown or grana <= 100 else 'Uhuuuu'
print(f'O status é: {status}')

#condicao satisfeita
grana = 130

status = 'Em casa' if lockdown or grana <= 100 else 'Uhuuuu'
print(f'O status é: {status}')
