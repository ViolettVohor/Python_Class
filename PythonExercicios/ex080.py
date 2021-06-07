val = []
for c in range(1, 6):
    inserir = int(input(f'Digite o {c}° valor: '))
    if c == 1:
        val.append(inserir)
        print('Adicionado ao final da lista...')
    else:
        for i in range(0, len(val)):
            if inserir <= val[i]:
                # Caso o valor digitado seja menor ou igual ao valor analisado ele será adicionado no lugar dele.
                val.insert(i, inserir)
                print(f'Adicionado na posição {i}')
                break
            elif inserir > val[i] == val[len(val)-1]:
                # Caso o valor digitado seja maior que o último valor então ele é adicionado no final
                val.append(inserir)
                print('Adicionado ao final da lista...')
print('-='*20)
print(f'Os valores digitados em ordem: {val}')
