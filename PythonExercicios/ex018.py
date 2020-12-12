from math import tan, cos, sin, radians
n = int(input('Digite um ângulo: '))
rad = radians(n)
print(f'O seno de \033[37;1m{n}\033[m vale \033[31;1m{sin(rad):.2f}\033[m \nO cosseno vale'
      f' \033[33;1m{cos(rad):.2f}\033[m \nE a tangente vale \033[32;1m{tan(rad):.2f}')
