nome = input('Digite seu nome completo: ').split()
print(f'Muito prazer em te conhecer!\nSeu primeiro nome é \033[1;32m{nome[0]}\033[m'
      f'\nE o último é \033[1;32m{nome[len(nome) - 1]}')
