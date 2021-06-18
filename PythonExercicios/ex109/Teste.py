from ex109 import Moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {Moeda.moeda(p)} é {Moeda.metade(p, True)}')
print(f'O dobro de {Moeda.moeda(p)} é {Moeda.dobro(p, True)}')
print(f'Aumentando 10%, {Moeda.moeda(p)} valerá {Moeda.aumentar(p, 10, True)}')
print(f'Diminuindo 13%, {Moeda.moeda(p)} valerá {Moeda.diminuir(p, 13, True)}')
