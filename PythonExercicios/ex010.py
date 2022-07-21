v = float(input('Quanto dinheiro você tem? R$'))
'''Mostrar quantos dólares ela pode comprar (utilizando a conversão)'''
d = v * 5.09
print('Com R${:.2f} você pode comprar EUR{:.2f}'.format(v,d))