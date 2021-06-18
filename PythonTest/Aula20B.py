def dobra(lst):  # Dobra os valores de uma lista
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


def contador(*num):  # Conta a quantidade de elemento, que foram passados como parâmetro
    tam = len(num)
    '''cont = 0
    for valor in num:
        cont += 1'''
    print(f'Recebi os números {num} que são {tam} ao todo')


def soma(a, b):  # Soma dois valores
    print(f'A = {a}, B = {b}')
    print(f'A soma de A + B = {a + b}')
    print('-'*30)


soma(b=4, a=5)  # Você não precisa informar os parâmetros na ordem
soma(8, 9)
soma(2, 1)
soma(a=4, b=1)

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)

# Exercícios 96 - 100
