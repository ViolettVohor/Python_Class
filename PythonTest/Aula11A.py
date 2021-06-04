print('\033[1;32mOlá, Mundo!\033[m')

a = 3
b = 5
print(f'Os valores são \033[32m{a}\033[m e \033[31m{b}\033[m!!!')

cores = {'limpa': '\033[m',
         'verde': '\033[32m',
         'amarelo': '\033[34m',
         'pretoebranco': '\033[7;30m',
         'negrito': '\033[1m'}

nome = 'Oliver'
print(f'Olá! Muito prazer em te conhecer, {cores["verde"]}{nome}{cores["limpa"]}!!!')

# Exercícios: Colocar cores em todos os exercícios até agora
