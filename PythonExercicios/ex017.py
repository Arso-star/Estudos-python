from math import pow, sqrt
co = int(input('Digite um valor: '))
ca = int(input('Digite outro valor: '))
h = sqrt(pow(co, 2) + pow(ca, 2))
print('Os valores entre {} e {}, a sua hipotenusa é {:.1f}.'.format(co, ca, h))