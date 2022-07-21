p = float(input('Digite o preço de um produto? R$')) #p significa o preço

'''Mostrar o seu novo preço com desconto'''
n = p - (p * 5 / 100)
print('O preço do produto custava R${:.2f}, o novo preço do produto com desconto de 5% é R${:.2f}'.format(p,n))