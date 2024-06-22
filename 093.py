jogador= {}
soma=0
partidas=list()
jogador['nome']=str(input('nome jogador:'))
tot=int(input(f'quants partidas {jogador["nome"]} jogou?'))
for c in  range(0,tot):
    partidas.append(int(input(f'quantos gols {jogador["nome"]} fez no {c} jogo:')))
    jogador['gols']=partidas[:]
jogador['total']=sum(partidas)
print('-='*30)
print(f'{jogador}')
print('-='*30)
for k,v in jogador.items():
    print(f'o campo {k} tem o valor {v}')
print('-='*30)
print(f'o jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for i,v in enumerate(jogador['gols']):
    print(f'        na partida {i} fez {v} gols')
print(f'foi um total de {jogador["total"]}')