print('Gerador de PA\n' + '-='*7)

a1 = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
cont = 1  # Index dos termos

while cont != 10:
    print(a1, end=' -> ')  # Mostra o termo atual
    a1 += r  # Adiciona a razão ao termo atual que se torna o próximo termo
    cont += 1
print('Acabou')
