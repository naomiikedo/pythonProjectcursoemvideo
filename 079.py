numeros=[]
while True:
    n=int(input('digite um numero:'))
    if n not in numeros:
        numeros.append(n)

        print('adicionado com sucesso')
    else:
        print('numero duplicado.nao adicionei a lista')
    r=str(input('deseja continuar?s/n'))
    if r in 'nN':
        break
numeros.sort()
print(f'voce digitou os valores:{numeros}')