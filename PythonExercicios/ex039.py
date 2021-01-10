from datetime import date
nasc = int(input('Ano de Nascimento: '))
sex = input('Qual seu sexo? [M/F]: ')
atual = date.today().year
ida = atual - nasc
alist = nasc + 18
if sex.upper() == 'M':
    print(f'Quem nasceu em \033[34;1m{atual}\033[m tem \033[34;1m{ida}\033[m anos em \033[34;1m{atual}\033[m')
    if ida == 18:
        print('Está na hora de\033[36;1m alistar')
    elif ida > 18:
        print(f'Passou(aram-se) \033[32;1m{ida - 18} ano(s)\033[m da hora de se alistar')
        print(f'Seu Alistamento foi em \033[36;1m{alist}')
    else:
        print(f'Falta(m) \033[31;1m{18 - ida} ano(s)\033[m até a hora de você se alistar')
        print(f'Seu Alistamento será em \033[36;1m{alist}')
else:
    print('Você\033[37;1m não precisa\033[m se alistar')
