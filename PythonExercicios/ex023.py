'''
num = int(input('Informe um número: '))
n = str(num)
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(n[3]))
print('Dezena: {}'.format(n[2]))
print('Centena: {}'.format(n[1]))
print('Milhar: {}'.format(n[0]))
'''

num = int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))

"""
num = int(input('Informe um número: '))
print('Analisando o número {}'.format(num))
unidade = num % 10
print('Unidade: {}'.format(unidade))
dezena = (num - unidade)/10
dezena = num % 100
print('Dezena: {}'.format(dezena))
centena = (num - dezena)/10
centena = num % 1000
print('Centena: {}'.format(centena))
milhar = (num - centena)/10
milhar = num % 10000
print('Milhar: {}'.format(milhar))
"""