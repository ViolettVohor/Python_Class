fr = input('Digite uma frase: ').strip().upper()
print(f'A letra "A" aparece {fr.count("A")} vezes nessa frase')
print(f'A primeira posição em que ela aparece é {fr.find("A") + 1}')
print(f'A última posição em que ela aparece é {fr.rfind("A") + 1}')
