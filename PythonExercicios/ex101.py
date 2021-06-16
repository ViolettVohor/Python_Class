from datetime import date


def votar(ano=2000):
    idade = date.today().year - ano
    if idade < 16:
        voto = 'NEGADO!'
    elif 18 > idade or idade > 65:
        voto = 'OPCIONAL'
    else:
        voto = 'OBRIGATÓRIO!'
    print(f'Com {idade} anos, ', end='')
    return voto


print('-'*30)
# noinspection SpellCheckingInspection
ano_nasc = int(input('Em que ano você nasceu? '))
print(f'sua situação de voto é {votar(ano_nasc)}')
