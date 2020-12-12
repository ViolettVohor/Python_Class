fr = input('Digite uma frase: ').strip().upper()
print(f'A letra "A" aparece \033[1;7;33m{fr.count("A")}\033[m vezes nessa frase')
print(f'A primeira posição em que ela aparece é \033[3m{fr.find("A") + 1}\033[m')
print(f'A última posição em que ela aparece é \033[3;32m{fr.rfind("A") + 1}\033[m')
