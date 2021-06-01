sexo = input('Digite o seu sexo [M/F]: ').upper().strip()[0]
# Pede ao usuário o sexo, remove os espaços no início e no final da frase,
# torna todas letras maiúsculas e pega a primeira letra

while sexo not in 'MF':  # Caso o usuário não digite M ou F ele pede para que ele introduza um valor válido.
    sexo = input('\033[31;1mDados inválidos.\033[m Por favor, informe seu sexo: ').upper().strip()[0]
print(f'Sexo \033[32;1m{sexo}\033[m registrado com sucesso')
