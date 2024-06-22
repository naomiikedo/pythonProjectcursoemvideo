n=[]
impar=[]
par=[]
while True:
    n.append(int(input('digite o numero:')))
    resp=str(input('deseja continuar?S/N:'))
    if resp  in 'nN':
        break
for i,v in enumerate(n):
    if v%2==0:
        par.append(v)
    else:
        impar.append(v)
print(f'a lista de numeros e : {n}')
print(f'os numeros pares sao : {par}')
print(f'os numeros impares sao: {impar}')