from datetime import date
ano = int(input('Digite o ano de nascimento do atleta: '))
id = date.today().year - ano
if id <= 9:
    cat = 'Mirim'
elif id <= 14:
    cat = 'Infantil'
elif id <= 19:
    cat = 'Junior'
elif id == 20:
    cat = 'Sênior'
else:
    cat = 'Master'
print(f'Esse atleta de \033[37;1m{id} anos\033[m está na \033[34;1mcategoria {cat}')
