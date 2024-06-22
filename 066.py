soma=0
tot=0
while True:
    n=int(input('digite um numero:'))
    if n==999:
        break
    soma+=n
    tot+=1
print(f'foram digitados {tot} numeros e a soma total dos numeros e {soma}')