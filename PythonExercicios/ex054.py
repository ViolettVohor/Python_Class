from datetime import date
data_atual = date.today()
ano_atual = data_atual.year  # Pega o ano atual do sistema
maior = 0

for i in range(0, 7):  # Verifica quem é maior de idade(21 anos) e quem é menor, entre um conjunto de 7 pessoas
    n = int(input('Digite o ano do seu nascimento: '))
    if ano_atual - n > 20:
        maior += 1
print(f'\033[36;1m{maior}\033[1m são maiores de idade \033[30;1me \033[37;1m{7 - maior}\033[1m são menores de idade')
