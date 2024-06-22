cont='zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessere','dezoito','dezenove','vinte'
while True:
    nu=int(input('digite um numero entre 0 e 20:'))
    if 0<= nu <=20:
        break
    print('tente novamente.',end='')
print(f'voce digitou o numero:{cont[nu]}')