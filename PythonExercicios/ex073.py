campeonato = 'Bragantino', 'Bahia', 'Ceará', 'Fortaleza', 'Athletico-PR', 'Flamengo', 'Atlético-GO', 'Cuiabá',\
    'Sport', 'Juventude', 'Internacional', 'São Paulo', 'Fluminense', 'Grêmio', 'Atlético-MG', 'América-MG',\
    'Palmeiras', 'Corinthians', 'Chapecoense', 'Santos'

print(f'Lista de times: {campeonato}\n' + '-='*20)  # Mostra os elementos da tupla
print(f'Os cinco primeiros são {campeonato[:5]}\n' + '-='*20)  # Mostra os cinco primeiros elementos da tupla
print(f'Os quatro últimos são {campeonato[-4:]}\n' + '-='*20)  # Mostra os últimos 4 elementos da tupla
print(f'Os times em ordem alfabética: {sorted(campeonato)}\n' + '-='*20)  # Mostra os elementos em ordem alfabética
print(f'O Chapecoense está na {campeonato.index("Chapecoense") + 1}° posição da tabela do Brasileirão')
# Mostra a posição da Chapecoense
