n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número:  '))
n3 = float(input('Digite o terceiro número: '))
# nl = [n1, n2, n3]
# print(f'O maior número é {max(nl)} \nE o menor é {min(nl)}')

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

print(f'O maior número é {maior} \nE o menor é {menor}')
