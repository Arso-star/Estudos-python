p = float(input('Digite o preço de um produto? ')) #p significa o preço
'''Mostrar o seu novo preço com desconto'''
l = int(input('A liquidação é em porcentagem? ')) #l - liquidação
o = int(input('A oferta será? '))
porcentagem = l/100
o = l - porcentagem #o - orfeta
pn = (p/o) #pn significa o seu novo preço
print('O preço novo do produto é R${:.2f}'.format(pn))