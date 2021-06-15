from random import randint
from time import sleep


def sorteia(lst):  # Sorteia 5 números e adiciona a lista do parâmetro
    print(f'Sorteando 5 valores da lista: ', end='')
    for i in range(0, 5):
        lst.append(randint(0, 50))
        print(lst[i], end=' ')
        sleep(0.5)
    print('PRONTO!')


def soma_par(lst):  # Soma os número pares da lista(parâmetro)
    soma = 0
    for num in lst:
        if num % 2 == 0:
            soma += num
    print(f'A soma dos números pares é: {soma}')


val = list()
sorteia(val)
soma_par(val)
