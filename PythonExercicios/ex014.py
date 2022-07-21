celsius = float(input('Digite o valor em Celsius: '))
fahrenheit = float(input('Digite o valor em Fahrenheit: '))
kelvin = float(input('Digite o valor em Kelvin: '))

f = 9 * celsius + 32 / 5
k = celsius + 273.15
fc = (fahrenheit - 32)/1.8
kc = kelvin - 273.15
fk = ((5 * fahrenheit) + 2297)/9
kf = ((9 * kelvin) - 2297)/5

print('O valor em {}ºC, foi convertido para {:.2f}ºF'.format(celsius,f))
print('O valor em {}ºC, foi convertido para {:.2f}ºK'.format(celsius,k))
print('O valor em {}ºF, foi convertido para {:.2f}ºC'.format(fahrenheit,fc))
print('O valor em {}ºK, foi convertido para {:.2f}ºC'.format(kelvin,kc))
print('O valor em {}ºF, foi convertido para {:.2f}ºK'.format(fahrenheit,fk))
print('O valor em {}ºK, foi convertido para {:.2f}ºF'.format(kelvin,kf))