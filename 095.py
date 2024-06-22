jogador= {}
time=list()
soma=0
partidas=list()
while True:
    jogador.clear()
    jogador['nome']=str(input('nome jogador:'))
    tot=int(input(f'quants partidas {jogador["nome"]} jogou?'))
    partidas.clear()
    for c in  range(0,tot):
        partidas.append(int(input(f'quantos gols {jogador["nome"]} fez no {c+1} jogo:')))
    jogador['gols']=partidas[:]
    jogador['total']=sum(partidas)
    time.append(jogador.copy())
    while True:
        resp=str(input('deseja continuar?[s/n]:')).upper()[0]
        if resp in 'SN':
            break
        print('erro.digite somente[s ou n]')
    if resp=='N':
        break
print('-='*30)
for k,v in enumerate(time):
    print(f'{k:>4} ',end='')
    for d in v.values():
        print(f'{str(d):<15}',end='')
    print()
print('-='*30)
while True:
    busca=int(input('qual jogador deseja analisar?'))
    if busca==999:
        break
    if busca >= len(time):
        print('ERRO.jogador nao existe')
    else:
        print(f'DADOS DO JOGADOR {time[busca]["nome"]}')
        for i,g in enumerate(time[busca]['gols']):
            print(f'no jogo {i+1} fez {g} gols')

