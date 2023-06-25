from twilio.rest import Client

account_sid = 'AC4c995d84e4895816aa5647dd37d98afa'
auth_token = '[AuthToken]'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:+14155238886',
  body='ola teste',
  to='whatsapp:+554198943254'
)

print(message.sid)

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
