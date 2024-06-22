maior=0
menor=99999
for c in range(1,6):
    peso=float(input('digite o peso:'))

    if peso>maior:
        maior=peso
    elif peso<menor:
        menor=peso
print('o maior peso digitado  foi {},e o menor foi {}'.format(maior,menor))