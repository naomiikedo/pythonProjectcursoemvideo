matriz=[[0,0,0],[0,0,0],[0,0,0]]
spar=maior=scol=0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c]=int(input(f'digite o {l,c} valor: '))
print('-'*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end='')
        if matriz[l][c]%2==0:
            spar+=matriz[l][c]
    print()
for l in range(0,3):
    scol+=matriz[l][2]
for c in range(0,3):
    if c==0:
        maior=matriz[1][c]
    elif matriz[1][c] > maior:
        maior=matriz[1][c]

print(f'a soma total dos numeros pares e: {spar}')
print(f'a soma da terceira coluna e: {scol}')
print(f'o maior numero digitado na segunda linha foi: {maior}')