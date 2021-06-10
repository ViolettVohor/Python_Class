alunos = []
while True:
    aluno = [input('Nome: '), [(float(input('Nota 1: '))), float(input('Nota 2: '))]]
    # Adiciona o nome do aluno e as notas a lista aluno
    alunos.append(aluno[:])  # Adiciona a lista aluno a lista alunos
    aluno.clear()  # Limpa a lista aluno
    '''nome = input('Nome: ')
    nota1 = float(input('Nota 1: '))  # Outra maneira de fazer o trecho acima
    nota2 = float(input('Nota 2: '))
    alunos.append([nome, [nota1, nota2]])'''
    
    while True:
        resp = input('Deseja continuar? [S/N] ').strip().upper()[0]
        if resp in 'SN':
            break
    if resp == 'N':
        break

print('-='*30)
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
print('-'*24)
for i, alu in enumerate(alunos):  # Mostra o número, o nome e a média dos alunos
    med = (alunos[i][1][0] + alunos[i][1][1])/2
    print(f'{i:<4}{alu[0]:<10}{med:>8}')
print('-'*24)

while True:  # Mostra as notas dos alunos
    esc = int(input('Quer ver as notas de qual aluno? (999 para interromper): '))
    if esc == 999:
        break
    if esc <= len(alunos) - 1:  # Caso seja digitado um número correspodente à um aluno
        print(f'Notas da(o) {alunos[esc][0]} são {alunos[esc][1]}')
    else:  # Caso não, é mostra essa mensagem
        print('Este aluno não foi cadastrado')
    print('-'*20)
print('FINALIZANDO...')
print('<<< Volte Sempre >>>')
