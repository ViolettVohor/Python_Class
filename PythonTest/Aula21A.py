def teste(b, ba=0):
    """
    Recebe dois valores númericos e mostra seu valores dentro do escopo local,
    mostra como mudar o valor de uma variável global dentro da função, sem
    criar uma variável local
    :param b: Parâmetro númerico
    :param ba: Parâmetro númerico e opcional
    :return: retorna 'soma' que é a soma de todos as variáveis dentro da função
    """
    global a  # Garante que a variável 'a' abaixo seja a variável 'a' global
    a = 8  # 'a' é uma variável de escopo local, quando a linha acima não é escrita
    b += 4
    c = 2
    soma = a + b + c + ba
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'BA dentro vale {ba}')  # Parâmetro opcional
    print(f'C dentro vale {c}')
    return soma  # Retorna a variável 'soma'


a = 5  # 'a' é uma variável de escopo global
r1 = teste(a)
print('='*30)
print(f'A fora vale {a}')

print(f'\nA soma dos valores é {r1}')
