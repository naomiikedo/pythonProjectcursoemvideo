lista=[]
dados=[]
tot=0

while True:
    dados.append(str(input('nome:')))
    dados.append((float(input('peso:'))))
    if len(lista)==0:
        pesado=leve=dados[1]
    else:
        if dados[1] > pesado:
            pesado=dados[0]
        elif dados[1]<leve:
            leve=dados[0]
    lista.append(dados[:])
    dados.clear()
    resp=str(input('deseja continuar?s/n:'))
    if resp in 'Nn':
        break
for c in lista:
    tot+=1

print(lista)
print(f'o total de de pessoas cadastradas e: {tot}')
print(f'as pessoas mais leves foram:{leve} e as mais pesadas foram {pesado}')
