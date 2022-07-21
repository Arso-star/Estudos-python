n = int(input('Digite qualquer valor: '))
x = 0
'''Como gerar a tabuada'''
print('=' * 18)
print('Tabuada de {}'.format(n))
print('=' * 18)

'''
t = x * n
print('{} x {} = {}'.format(x,n,t))
x += 1
'''
while x <= 10:
    print('{} X {} = {}'.format(x,n,(x * n)))
    x += 1