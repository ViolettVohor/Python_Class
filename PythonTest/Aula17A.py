num = [2, 5, 9, 1]  # Lista
num[2] = 3  # Substituí o elemento na posição dois pelo valor 3
num.append(7)  # Adicionar o valor 7 no final da lista
num.sort(reverse=True)  # Organiza os elementos do maior para o menor
num.insert(2, 2)  # Insere o valor dois na segunda posição deslocando os outros elementos
if 4 in num:
    num.remove(4)  # Remove o elemento 4
else:
    print('Não achei o número 4')
num.pop(2)  # Remove o elemento na posição 2

print(num)
print(f'Essa lista tem {len(num)} elementos')  # Mostra o comprimento da lista

# Exercício 78 - 83
