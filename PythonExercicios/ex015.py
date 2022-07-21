km = float(input('Quantos Km rodados? '))
dias = float(input('Quantos dias alugados? '))

valorKm = km * 0.15
valorAluguel = 60 * dias
valorTotal = valorKm + valorAluguel

print('O valor total é R${:.2f}, sendo R${:.2f} ao Km rodados e R${:.2f} aos dias alugados'.format(valorTotal, valorKm, valorAluguel))


'''
km = float(input('Quantos Km rodados? '))
dias = int(input('Quantos dias alugados? '))

valorTotal = (km * 0.15) + (60 * dias)

print('O valor total é R${:.2f}.'.format(valorTotal))
'''