nome = input('Qual é seu nome? ').upper().strip()
if nome == 'OLIVER':
    print('Que nome bonito!')
elif nome == 'MATHEUS' or nome == 'LUCAS' or nome == 'EDUARDA':
    print('Seu nome é bem popular no Brasil')
elif nome in 'MADELEINE OLIVIA MARY SAM PEARL':
    print('Que belo nome feminino!')
# else:
#     print('Seu nome é bem normal!')
print(f'Tenha um bom dia, \033[36;1m{nome}!')

# Exercícios: 36 - 45
