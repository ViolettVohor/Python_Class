from datetime import date
ano = int(input('Digite um ano (Digite 0 para analisar o ano atual): '))
ano = date.today().year if ano == 0 else ano
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'\033[1;37m{ano}\033[m é Bissexto.')
else:
    print(f'\033[1;37m{ano}\033[m não é Bissexto.')
