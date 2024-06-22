v=int(input('qual a velocidade do carro?'))
if v >80:
    vm=v-80
    multa=7*vm
    print('voce estava acima do limite de velocidade e pagara {} de multa'.format(multa))
else:
    print('voce estava no limite de velocidade')