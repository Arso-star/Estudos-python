"""Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR."""

numero = int(input('Me diga um número qualquer: '))

res = numero % 2

if res == 0:
    print('O resto de {} é igual a {}. É PAR!'.format(numero, res))
else:
    print('O resto de {} é igual a {}. É ÍMPAR!'.format(numero, res))