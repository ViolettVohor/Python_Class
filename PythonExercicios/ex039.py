ida = int(input('Qual a idade do jovem? '))
if ida == 18:
    print('Está na hora de \033[36;1malistar')
elif ida > 18:
    print(f'Passaram-se \033[32;1m{ida - 18} anos\033[m da hora de se alistar')
else:
    print(f'Faltam \033[31;1m{18 - ida} anos\033[m até a hora de se alistar')
