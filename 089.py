ficha=[]
while True:
    nome=str(input('nome:'))
    nota1=float(input('nota1:'))
    nota2=float(input('nota2:'))
    media= (nota1+nota2) /2
    ficha.append([nome,[nota1,nota2],media])
    resp=str(input('deseja continuar?S/N:'))
    if resp  in 'Nn':
        break
print('-'*30)
print(f'{"No.":<4}{"nome":<10}{"Media":>8}')
print('-'*26)
for i,a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*30)
    opc=int(input('mostrar notas de qual aluno?999 para o programa'))
    if opc == 999:
        break
    if opc <= len(ficha) -1:
        print(f'notas de {ficha[opc][0]} sao {ficha[opc][1]}')
print('volte sempre')
