din = float(input('Quanto dinheiro você tem na carteira? R$'))
# Pede que o usuário digite a quantidade de dinheiro que tem na carteira, transforma
# no tipo float e armazena na variável

print(f'Você pode comprar \033[33;40;1mUS${din/5.37:.2f}\033[m')
# Fundo branco (40) e fonte amarela (33) e negrito (1)
# Mostra a quantidade de dólares que é possível comprar
