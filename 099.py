def maior(*num):
    cont=maio=0
    for n in num:
        print(f'{n} ',end='')
        if n > maio:
            maio=n

    print(f' foram digitados {len(num)} numeros e o maior e {maio} ')
maior(1,7,3,2,11)
maior(2,3,4,5,6,7,8,9,23,71)
maior(0,0,1)