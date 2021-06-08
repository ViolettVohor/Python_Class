matriz = [[], [], []]
for lin in range(0, 3):
    for col in range(0, 3):
        matriz[lin].append(int(input(f'Digite um valor para [{lin}, {col}]: ')))

print('-='*30)
for lin in matriz:
    for col in lin:
        print(f'[  {col}  ]', end=' ')
    print()
