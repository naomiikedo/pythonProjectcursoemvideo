numero=[]
while True:
    numero.append(input('digite um numero:'))
    c=str(input('deseja continuar?s/n:'))
    if c in 'Nn':
        break
numero.sort(reverse=True)
print(f'voce digitou os numeros {numero}')
print(f'foram digitados {len(numero)} numeros')
if 5 in numero:
    print('o numero 5 esta na lista')
else:
    print('nao achei o numero 5 na lista')
