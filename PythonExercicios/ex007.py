n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
print(f'A média desse aluno que tirou \033[32;1m{n1:.1f}\033[m e '
      f'\033[32;1m{n2:.1f}\033[m, foi \033[32;1m{(n1 + n2) / 2:.1f}')
