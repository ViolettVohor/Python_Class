from math import trunc
n = int(input('Digite um número entre 0 e 9999: '))
m1 = trunc(n/1000)
c2 = trunc(n/100)
d2 = trunc(n/10)
c1 = c2 - m1 * 10
d1 = d2 - m1 * 100 - c1 * 10
print(f"""Unidade: {n - m1 * 1000 - c1 * 100 - d1 * 10}
Dezena: {d1}
Centena: {c1}
Milhar: {m1}""")

# u = n % 10
# d = n // 10 % 10
# c = n // 100 % 10
# m = n // 1000
# print(f'Unidade: {u}\n'
#       f'Dezena: {d}\n'
#       f'Centena: {c}\n'
#       f'Milhar: {m}')
