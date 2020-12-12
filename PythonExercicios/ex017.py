# from math import sqrt, pow
from math import hypot
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjascente: '))
# hip = sqrt(pow(co, 2) + pow (ca, 2))
hip = hypot(co, ca)
print(f'A hipotenusa desse triângulo vale \033[35;1m{hip:.2f}')
