
while True:
    tabuada = int(input('deseja saber a tabuada de qual valor?'))
    if tabuada<0:
        break
    for c in range(1,11):
        print(f'{tabuada}*{c}={tabuada*c}')
print('FIM DO PROGRAMA')
