"""
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.
"""
sal_funcionario = float(input('Digite o salário do funcionário: R$'))

if sal_funcionario > 1250:
    sup = sal_funcionario + (sal_funcionario * 10 / 100)
    print('O salário original do funcionário era R${:.2f}, o novo salário de 10% de aumento recebe R${:.2f}'.format(sal_funcionario, sup))
if sal_funcionario <= 1250:
    inf = sal_funcionario + (sal_funcionario * 15 / 100)
    print('O salário original do funcionário era R${:.2f}, o novo salário de 15% de aumento recebe R${:.2f}'.format(sal_funcionario, inf))