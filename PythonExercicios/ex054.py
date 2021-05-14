from datetime import date
ano_atual = date.today().year  # Pega o ano atual do sistema
maior = 0

for i in range(1, 8):  # Verifica quem é maior de idade(21 anos) e quem é menor, entre um conjunto de 7 pessoas
    n = int(input(f'Digite o ano de nascimento da {i}° pessoa: '))
    if ano_atual - n > 20:
        maior += 1
print(f'\033[36;1m{maior}\033[1m são maiores de idade \033[30;1m'
      f'\nE \033[37;1m{7 - maior}\033[1m são menores de idade')
