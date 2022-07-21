n1 = int(input('Primeiro valor: '))
n2 = int(input('Outro valor: '))
s = n1+n2
sub = n1-n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2
r = n1%n2
print('A soma é igual a {}, a subtração é {}, a multiplicação é {}, a divisão é {:.2f}!'.format(s,sub,m,d), end=' >>> ')
print('A divisão inteira é {}, a exponenciação é {} e o resto é {}!'.format(di,e,r))