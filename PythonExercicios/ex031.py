"""
Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
"""

distância = float(input('Qual é a distância de sua viagem? '))

if distância >= 200:
    viagem = distância * 0.45
else:
    viagem = distância * 0.50

"""
viagem = distância * 0.50 if distância <= 200 else distância * 0.45
"""
print('Você está prestes a começar uma viagem de {} Km.'.format(distância))
print('E o preço da passagem será de R$ {:.2f}'.format(viagem))