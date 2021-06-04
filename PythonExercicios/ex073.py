campeonato = 'Bragantino', 'Bahia', 'Ceará', 'Fortaleza', 'Athletico-PR', 'Flamengo', 'Atlético-GO', 'Cuiabá',\
    'Sport', 'Juventude', 'Internacional', 'São Paulo', 'Fluminense', 'Grêmio', 'Atlético-MG', 'América-MG',\
    'Palmeiras', 'Corinthians', 'Chapecoense', 'Santos'

print('Os cinco primeiros são', campeonato[:5], '\n' + '-='*20)
print('Os quatro últimos são', campeonato[-4:], '\n' + '-='*20)
print('Os times em ordem alfabética:', sorted(campeonato), '\n' + '-='*20)
print(f'O Chapecoense está na {campeonato.index("Chapecoense") + 1}° posição da tabela do Brasileirão')
