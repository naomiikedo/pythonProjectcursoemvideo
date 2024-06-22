soma=0
for c in range(1,7):
    n=int(input('digite o numero:'))
    if n%2==0:
        soma=soma+n
print('a soma total dos numeros pares e {}'.format(soma))