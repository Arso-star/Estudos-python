"""
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
"""
print('-=-' * 12)
print('Analisador de Triângulos')
print('-=-' * 12)

a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if a + b > c and a + c > b and b + c > a:
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')

"""
if a + b > c:
    print('Os segmentos acima PODEM FORMAR triângulo!')
elif a + c > b:
    print('Os segmentos acima PODEM FORMAR triângulo!')
elif b + c > a:
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')
"""