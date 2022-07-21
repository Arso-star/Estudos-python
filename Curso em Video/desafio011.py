largura = float(input('Qual é a largura em metros? '))
altura = float(input('Qual é a altura em metros? '))
'''Como calcular a sua área e a quantidade de tinta necessária para pintar em litros'''
area = largura * altura #Calculamos a área da parede em metros ao quadrados
rend = int(input('Rendimento fabricante em m² por litros? ')) #Saber o rendimento em litros
d = int(input('Quantidade necessária de demão? ')) #Saber a quantidade para o rendimento
quantidade = area * 2
quantidade = quantidade/10
print('A área para pintar é {:.2f}m²'.format(area))
print('A quantidade de tinta necessária será {:.2f}l'.format(quantidade))