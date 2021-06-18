teste = list()

teste.append('Matheus')
teste.append(17)
galera = [teste[:]]  # Cria uma copia de teste dentro de galera
teste[0] = 'Oliver'
teste[1] = 22
galera.append(teste)  # Cria um vínculo entre teste e galera
print(galera)

pessoas = [['Harvey', 23], ['Madeleine', 19], ['Roger', 250], ['Mark', 20]]
print(pessoas[0][0])  # Mostra o primeiro valor da primeira lista desta lista
for p in pessoas:
    print(f'{p[0]} tem {p[1]} anos de idade.')

dados = []
pes = []
for i in range(0, 3):
    print('-='*10)
    dados.append(input('Nome: '))
    dados.append(int(input('Idade: ')))
    pes.append(dados[:])
    dados.clear()  # Excluí os valores dentro de dados

for p in pes:
    print(f'{p[0]} é maior de idade.' if p[1] > 20 else f'{p[0]} é menor de idade.')

# Exercício 84 -89
