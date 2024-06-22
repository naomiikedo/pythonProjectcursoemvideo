times='america-MG','atletico-PR','atletico-GO','atletico-MG','avai','botafogo','ceara','corinthians','coritiba','cuiaba','flamengo','fluminense','fortaleza','goiais','internacional','juventude','palmeiras','bragantino','santos','sao paulo'
print(f'lista dos times:{times}')
print(f'os 5 primeiros colocados sao:{times[0:5]}')
print(f'os 4 ultimos sao:{times[-4:]}')
print(f'times em ordem alfabetica:{sorted(times)}')
print(f'posicao do botafogo e {times.index("botafogo")+1}')