import urllib
import urllib.request
try:
   site=urllib.request.urlopen('http://www.pudim.com.br')
except :
    print('erro')
else:
    print('tudo ok')