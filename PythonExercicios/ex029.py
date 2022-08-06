"""
Escreva um programa que leia a velocidade de um carro. 
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.
"""

carro = float(input('Qual a velocidade atual do carro? '))

km = 80
valorMulta = (carro - 80) * 7

if carro <= km:
    print('Tenha um bom dia! Dirija com segurança!')
else:
    print('MULTADO! Você excedeu o limite permitido que é de {} Km/h'.format(km))
    print('Você deve pagar uma multa de R$ {:.2f}'.format(valorMulta))