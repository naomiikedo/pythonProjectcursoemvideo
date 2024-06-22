galera=[]
dados=[]
menor=maior=0
for c in range(0,3):
    dados.append(str(input('nome:')))
    dados.append(int(input('idade:')))
    galera.append(dados[:])
    dados.clear()
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} e maior de idade')
        maior=maior+1
    else:
        print(f'{p[0]} e menor de idade')
        menor=menor+1
print(f'{menor} menores de idade e {maior} maiores de idade')