valores=[]
for cont in range(0,5):
    valores.append(int(input('digite um numero:')))
for c,v in enumerate(valores):
    print(f'encontrei {v} na posicao {c}')