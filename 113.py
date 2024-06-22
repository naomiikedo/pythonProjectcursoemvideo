def leiaint(msg):
    while True:
        try:
            n=int(input(msg))
        except(ValueError,TypeError):
            print('erro.tente um numero inteiro valido')
            continue
        else:
            return n


def leiaf(n):
    while True:
        try:
            f=float(input(n))
        except(ValueError,TypeError):
            print('erro.tente um numero real valido')
            continue
        else:
            return f



num=leiaint('digite um valor inteiro:')
real=leiaf('digite um valor real:')
print(f'o numero inteiro digitado foi:{num} e o numero real foi:{real}')
