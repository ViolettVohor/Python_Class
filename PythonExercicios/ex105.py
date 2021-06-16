def notas(*num, sit=False):
    """
    -> Função para analisar notas e situação de vários alunos
    :param num: uma ou mais notas dos alunos (aceita várias)
    :param sit: (opcional) indica se deve ou não mostrar a situação
    :return: dicionário com dados da turma.
    """
    dados = {'Quantidades de notas': len(num),
             'Maior nota': max(num),
             'Menor nota': min(num)}
    soma = 0
    for n in num:
        soma += n

    dados['Média da Turma'] = soma / len(num)
    if sit:
        if dados['Média da Turma'] > 7:
            dados['Situação'] = 'Boa'
        elif dados['Média da Turma'] > 5:
            dados['Situação'] = 'Razoável'
        else:
            dados['Situação'] = 'Ruim'

    return dados


resp = notas(3.5, 2, 6.5, 2, 7, 4, sit=True)
print(resp)
