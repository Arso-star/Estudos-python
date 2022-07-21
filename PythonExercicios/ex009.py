n = int(input('Digite qualquer valor: '))

'''Como gerar a tabuada'''
print('=' * 13)
print('Tabuada de {}'.format(n))
print('-' * 12)
print('{} x {:2} = {}'.format(n, 0, n * 0))
print('{} x {:2} = {}'.format(n, 1, n * 1))
print('{} x {:2} = {}'.format(n, 2, n * 2))
print('{} x {:2} = {}'.format(n, 3, n * 3))
print('{} x {:2} = {}'.format(n, 4, n * 4))
print('{} x {:2} = {}'.format(n, 5, n * 5))
print('{} x {:2} = {}'.format(n, 6, n * 6))
print('{} x {:2} = {}'.format(n, 7, n * 7))
print('{} x {:2} = {}'.format(n, 8, n * 8))
print('{} x {:2} = {}'.format(n, 9, n * 9))
print('{} x {:2} = {}'.format(n, 10, n * 10))
print('-' * 12)

'''
t = x * n
print('{} x {} = {}'.format(x,n,t))
x += 1

while x <= 10:
    print('{} X {} = {}'.format(x,n,(x * n)))
    x += 1
'''