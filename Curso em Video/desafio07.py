n1 = int(input('A primeira nota é: '))
n2 = int(input('A segunda nota é: '))
m = (n1 + n2) / 2
print('A média é {}'.format(m))
if m > 7:
    print('Aprovado!!')
else:
    print('Reprovado!!')
