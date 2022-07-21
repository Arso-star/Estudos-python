'''Média aritmética'''
n1 = float(input('A primeira nota é: '))
n2 = float(input('A segunda nota é: '))
print('A média entre {:.1f} e {:.1f} é {:.1f}'.format(n1,n2,(n1+n2)/2))
if (n1+n2)/2 >= 7:
    print('Aprovado!!')
else:
    print('Reprovado!!')