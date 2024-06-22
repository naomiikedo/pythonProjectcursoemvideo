valores=[]
maior=0
menor=0
for cont in range(0,5):
    valores.append(int(input(f'digite o {cont} valor:')))
    if cont == 0:
        menor = maior =valores[cont]
    else:
        if valores[cont] > maior:
            maior=valores[cont]
        if valores[cont]<menor:
            menor=valores[cont]
print(f'o maior numero digitado foi {maior} na posicao ',end='')
for i,v  in enumerate(valores):
    if v ==maior:
       print(f'{i}...',end='')
print()
print(f'o menor numero e {menor} na posicao ',end='')
for i,v in enumerate(valores):
    if v==menor:
        print(f'{i}...',end='')
print()