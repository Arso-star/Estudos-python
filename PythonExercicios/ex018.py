
from math import radians, sin, cos, tan
num = float(input('Digite um ângulo qualquer: '))

seno = sin(radians(num))
cosseno = cos(radians(num))
tangente = tan(radians(num))

print('O ângulo de {} do seno é igual a {:.2f}'.format(num, seno))
print('O ângulo de {} do cosseno é igual a {:.2f}'.format(num, cosseno))
print('O ângulo de {} do tangente é igual a {:.2f}'.format(num, tangente))


'''
from math import hypot
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))

hi = hypot(co, ca)

seno = co/hi
cosseno = ca/hi
tangente = co/ca

print('Os valores entre {} e {}, a hipotenusa é igual a {:.2f}'.format(co, ca, hi))
print('O ângulo do cateto oposto {} para seno é igual a {:.2f}'.format(co, seno))
print('O ângulo do cateto adjacente {} para cosseno é igual a {:.2f}'.format(ca, cosseno))
print('O ângulo do cateto oposto {} e o ângulo do cateto adjacente {} para tangente é igual a {:.2f}'.format(co, ca, tangente))
'''