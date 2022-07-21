largura = float(input('Qual é a largura da parede em metros? '))
altura = float(input('Qual é a altura da parede em metros? '))

'''Como calcular a sua área e a quantidade de tinta necessária para pintar em litros'''

area = largura * altura  #Calculamos a área da parede em metros ao quadrados
tinta = area / 2 #Calcular a quantidade de litros
print('A parede tem a dimensão de {:.2f} x {:.2f} e sua área é {:.2f}m².'.format(largura,altura,area))
print('Para pintar a parede, você precisará de {:.2f}l de tinta.'.format(tinta))