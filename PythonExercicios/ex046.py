import time
for c in range(10, -1, -1):  # Fazer uma contagem regressiva de 10 até 0
    print(f'\033[37m{c}')  # mostra o valor de c
    time.sleep(1)  # Pausa o programa por um segundo
print('\033[33;1m🎆🎆🎆🎆🎆\033[32;1mKaboom\033[33;1m🎆🎆🎆🎆🎆')
