mt = float(input('Digite uma distância em Metros: '))
# Pedi que o usuário digite uma distância em metros e armazena na variável

print(f'Essa distância convertida vale \033[36;1m\n{mt/1000}km \n{mt/100}hm \n{mt/10}dam \n{mt*10}dm '
      f'\n{mt*100}cm \n{mt*1000}mm')
# Mostra essa distância convertida para kilometros, hectometros, decâmetros, decimetros, centímetros e milimetros
# medidas em turquesa (36)
