# import Funcoes
from Aula22.Uteis.Numeros.__init__ import fatorial, dobro
# Não recomendado, pois caso seja importado vários módulos pode haver conflitos com os nomes
# Pacotes = Bibliotecas

n = int(input('Digite um número: '))
fat = fatorial(n)
print(f'O fatorial de {n} é {fat}')
print(f'O dobro de {n} é {dobro(n)}')

# Exercícios 107 -112
