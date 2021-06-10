matriz = [[], [], []]
# matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for lin in range(0, 3):  # Representa as 3 linhas da matriz
    for col in range(0, 3):  # Representa as 3 colunas da matriz
        matriz[lin].append(int(input(f'Digite um valor para [{lin}, {col}]: ')))  # Adiciona os valor a matriz
        # matriz[lin][col] = int(input(f'Digite...

print('-='*30)
for lin in matriz:  # for lin in range(0, 3):  # Percorre as linhas da matriz
    for col in lin:  # for col in range(0, 3):  # Percorre as colunas de cada linha
        print(f'[{col:^5}]', end=' ')
    print()
