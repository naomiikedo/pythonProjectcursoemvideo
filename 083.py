exp=str(input('digite a expressao:'))
lista=[]
for simb in exp:
    if simb=='(':
        lista.append('(')
    elif  simb==(')'):
        if len(lista)>0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista)==0:
    print('sua expressao e valida')
else:
    print('sua expressao nao e valida')

