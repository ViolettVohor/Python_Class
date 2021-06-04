lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita'  # Tuplas são Imutáveis
# lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
# lanche[1] = 'Água'
print(lanche[:3])  # O terceiro elemento é ignorado
print(lanche[-3:])  # Do Terceiro elemento, de trás para frente, até o final
print(len(lanche), '\n')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}!, na posição {cont}')

print('')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida}!, na posição {pos}')
print('Comi pra caramba')

print(f'\n{sorted(lanche)}')

a = 2, 5, 4
b = 5, 8, 1, 2
c = b + a
print(c)
print(c.count(5))
print(c.index(5, 1))  # Mostra o index do número 5 apartir da posição 1

pessoa = 'Matheus', 18, 'M', 60  # No python, as tuplas aceitam valores de tipos diferentes
# del(pessoa)  # Deleta a tupla pessoa
print(pessoa)
