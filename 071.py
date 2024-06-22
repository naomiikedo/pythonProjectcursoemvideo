valor=int(input('quanto deseja sacar?'))
total=valor
ced=50
totc=0
while True:
    if total >=ced:
        total-=ced
        totc+=1
    else:
        print(f'total de {totc} cedulas de {ced}')
        if ced==50:
            ced=20
        elif ced ==20:
            ced=10
        elif ced==10:
            ced=1
        totc=0
        if total==0:
            break
