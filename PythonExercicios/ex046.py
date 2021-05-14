from time import sleep
for i in range(10, -1, -1):  # Faz uma contagem regressiva de 10 até 0
    print(f'\033[37m{i}')  # Mostra o valor de i
    sleep(1)  # Pausa o programa por um segundo
print('\033[33;1m🎆🎆🎆🎆🎆\033[32;1mKaboom\033[33;1m🎆🎆🎆🎆🎆')
