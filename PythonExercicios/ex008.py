m = float(input('Digite o valor em metros: '))
'''Como converter em centímetros e milímetros'''
print('{}km'.format(m / 1000))
print('{}hm'.format(m / 100))
print('{}dam'.format(m / 10))
print('{:.0f}m'.format(m))
print('{:.0f}dm'.format(m * 10))
print('{:.0f}cm'.format(m * 100))
print('{:.0f}mm'.format(m * 1000))
#print('A medida de {}m em centímetros é {:.0f}cm e em milímetros é {:.0f}mm'.format(m,(m * 100),(m * 1000)))