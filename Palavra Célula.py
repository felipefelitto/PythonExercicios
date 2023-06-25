from twilio.rest import Client

sid='AC4c995d84e4895816aa5647dd37d98afa'
auth='864dfd4f02d129c239a12b672d22f68f'
client=Client(sid,auth)
client.api.account.messages.create(to='whatsapp:+554198943224',
                               from_='whatsapp:+14155238886',
                               body="Olá Felipe, Voce criou o primeiro robo")

"""message=client.messages.create(to='whatsapp:+5541998943254',
                               from_='whatsapp:+17602497880',
                               body="Olá Felipe, Voce criou o primeiro robo")"""


'''import random
from datetime import date
from calendar import monthrange

#número de casais na célula que levam a palavra e escala
n=[]
cont=1
j=int(input(('Quantos casais que levam a palavra tem na célula? ')))
while   (cont<=j):
    n.append(0)
    n[cont-1]=input('Qual o nome do {}º casal? '.format (cont))
    cont=cont+1
random.shuffle(n)

#quantas segundas tem no mês
m=int(input ('Qual é o mês de 2023 que será feito a escala? (escrever númerico) '))
last_day=monthrange(2023,m)
d=1
dd=[]
cont1=0
while d<=last_day[1]:
    data = date(year=2023, month=m, day=d)
    if data.weekday()==0:
        cont1=cont1+1
        dd.append(d)
    d=d+1
print ('O mês tem {} segundas-feiras'.format (cont1))

cont2=1
while (cont2<=cont1):
    print('O {}º casal a levar a palavra é {} no dia {}/{}/2023'.format(cont2, n[cont2-1],dd[cont2-1],m))
    cont2=cont2+1
    n=n*cont2
'''