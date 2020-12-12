n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número:  '))
n3 = float(input('Digite o terceiro número: '))
# nl = [n1, n2, n3]
# print(f'O maior número é \033[1;32m{max(nl)}\033[m \nE o menor é \033[31;1m{min(nl)}\033[m')

maior = n2
if n1 > n2 and n1 > n3:
    maior = n1
if n3 > n2 and n3 > n1:
    maior = n3

menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

print(f'O maior número é \033[32;1m{maior}\033[m \nE o menor é \033[31;1m{menor}')
