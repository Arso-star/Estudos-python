import __main__

def mdc(a, b, resto):
    while b != 0:
        resto = a % b
        a = b
        b = resto
    return a

if __name__ == '__main__':
    var =  n, f1, f2
    while i > 0:
        print(' ', mdc(f1,f2))
        i--
