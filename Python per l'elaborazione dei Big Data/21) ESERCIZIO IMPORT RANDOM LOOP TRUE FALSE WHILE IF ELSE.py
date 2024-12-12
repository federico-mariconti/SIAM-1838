'''
esercizio
il computer pensa a un numero tra 0 e 9
tento di indovinarlo
se indovino il programma stampa un messaggio e termina
se non indovino devo riprovare a dare una nuova risposta
'''
import random

cpunum=0
cpunum=random.randint(1,90)

print(cpunum)

LOOP=True
while LOOP:
    usernum=int(input('indovina il numero: '))
    if (cpunum==usernum):
        print(f'esatto ho pensato il num {cpunum} e hai indovinato con il num {usernum}')
        LOOP=False #potevo anche mettere break al posto di LOOP=False
    else:
        print('sbagliato ritenta')
        

        



