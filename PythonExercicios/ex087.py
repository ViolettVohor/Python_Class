matriz = [[], [], []]
# noinspection SpellCheckingInspection
somapar = somacol = 0
for lin in range(0, 3):
    for col in range(0, 3):
        matriz[lin].append(int(input(f'Digite um número para [{lin}, {col}]: ')))
        if matriz[lin][col] % 2 == 0:  # Caso o número inserido for par
            somapar += matriz[lin][col]  # ele é adiciona a soma dos pares

print('-='*30)
for lin in matriz:
    # noinspection SpellCheckingInspection
    for icol, col in enumerate(lin):
        print(f'[  {col}  ]', end=' ')
        if icol == 2:  # Se for a terceira coluna
            somacol += col  # o valor é adiciona a soma dos valores da terceira coluna
    print()

print('-='*30)
print(f'A soma de todos os valores pares vale {somapar}')
print(f'A soma de todos os valores da terceira coluna vale {somacol}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')  # Mostra o maior valor da segunda linha
