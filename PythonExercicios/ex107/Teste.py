from ex107 import Moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {p} é {Moeda.metade(p)}')
print(f'O dobro de {p} é {Moeda.dobro(p)}')
print(f'Aumentando 10%, {p} valerá {Moeda.aumentar(p, 10)}')
print(f'Diminuindo 13%, {p} valerá {Moeda.diminuir(p, 13)}')
