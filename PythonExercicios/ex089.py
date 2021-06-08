alunos = []
while True:
    aluno = [input('Nome: ')]
    nota = [(float(input('Nota 1: '))), float(input('Nota 2: '))]
    aluno.append(nota[:])
    alunos.append(aluno[:])
    aluno.clear()
    nota.clear()
    
    while True:
        resp = input('Deseja continuar? [S/N] ').strip().upper()[0]
        if resp in 'SN':
            break
    if resp == 'N':
        break

print('-='*30)
print(f'{"No.":<3}{"Nome":<10}{"Média":>5}')
print('-'*20)
for i, alu in enumerate(alunos):
    med = (alunos[i][1][0] + alunos[i][1][1])/2
    print(f'{i:<3}{alunos[i][0]:<10}{med:>5}')
print('-'*20)

while True:
    esc = int(input('Quer ver as notas de qual aluno? (999 para interromper): '))
    if esc == 999:
        break
    print(f'Notas da(o) {alunos[esc][0]} são {alunos[esc][1]}')
    print('-'*20)
print('FINALIZANDO...')
print('<<< Volte Sempre >>>')
