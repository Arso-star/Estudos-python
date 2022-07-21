funcionário = float(input('Digite o seu salário: R$'))

'''Mostrar o novo salário do funcionário, com 15% de aumento'''
novo = funcionário + (funcionário * 15/100)
print('O salário original do funcionário era R${:.2f}, o novo salário de 15% de aumento recebe R${:.2f}'.format(funcionário,novo))