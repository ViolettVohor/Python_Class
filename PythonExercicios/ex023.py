from math import trunc
n = int(input('Digite um número entre 0 e 9999: '))
m1 = trunc(n/1000)
c2 = trunc(n/100)
d2 = trunc(n/10)
c1 = c2 - m1 * 10
d1 = d2 - m1 * 100 - c1 * 10
print(f"""Unidade: \033[1;31m{n - m1 * 1000 - c1 * 100 - d1 * 10}\033[m
Dezena : \033[32;1m{d1}\033[m
Centena: \033[33;1m{c1}\033[m
Milhar : \033[34;1m{m1}\033[m""")

# u = n % 10
# d = n // 10 % 10
# c = n // 100 % 10
# m = n // 1000
# print(f'Unidade: \033[32;1m{u}\033[m\n'
#       f'Dezena : \033[33;1m{d}\033[m\n'
#       f'Centena: \033[344;1m{c}\033[m\n'
#       f'Milhar : \033[31;1m{m}\033[m')
