lista=[[],[]]
valor=0
for c in range(0,7):
    valor=(int(input('digite um numero:')))
    if valor %2==0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
print(f'lista completa e {lista}')
lista[0].sort()
lista[1].sort()
print(f'numeros pares sao:{lista[0]}')
print(f'numeros impares sao:{lista[1]}')