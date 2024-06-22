from random import randint
def sorteia(lista):
    for cont in range(0,5):
        lista.append(randint(1,10))

def somapar(lista):
    soma=0
    for v in lista:
        if v %2==0:
            soma+=v
    print(f'somando os valores da lista {lista} a soma dos pares e {soma}')


numeros=list()
sorteia(numeros)
print(numeros)
somapar(numeros)