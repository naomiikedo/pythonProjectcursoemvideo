def ficha(jog='desconhecido',gols=0):
    print(f'o jogador {jog} fez {gols} gols no campeonato')
n=str(input('nome do jogador:'))
g=str(input('gols:'))
if g.isalnum():
    g=int(g)
else:
    g=0
if n.strip() =='':
    ficha(gols=g)
else:
    ficha(n,g)