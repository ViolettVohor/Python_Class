from datetime import date
ano = int(input('Digite o ano de nascimento do atleta: '))
ida = date.today().year - ano
if ida <= 9:
    cat = 'Mirim'
elif ida <= 14:
    cat = 'Infantil'
elif ida <= 19:
    cat = 'Junior'
elif ida <= 25:
    cat = 'Sênior'
else:
    cat = 'Master'
print(f'Esse atleta de \033[37;1m{ida} anos\033[m está na\033[34;1m categoria {cat}')
