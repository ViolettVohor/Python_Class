def votar(ano=2000):
    """
    -> Verifica a situação de voto de acordo com o ano de nascimento da pessoa
    :param ano: ano de nascimento da pessoa, (padrão ano 2000)
    :return: Retorna a situação da pessoa
    """
    from datetime import date

    idade = date.today().year - ano
    print(f'Com {idade} anos, sua situação se voto é ', end='')
    if idade < 16:
        return 'NEGADO!'
    elif 18 > idade or idade > 65:
        return 'OPCIONAL'
    else:
        return 'OBRIGATÓRIO!'


print('-'*30)
# noinspection SpellCheckingInspection
ano_nasc = int(input('Em que ano você nasceu? '))
print(votar(ano_nasc))
