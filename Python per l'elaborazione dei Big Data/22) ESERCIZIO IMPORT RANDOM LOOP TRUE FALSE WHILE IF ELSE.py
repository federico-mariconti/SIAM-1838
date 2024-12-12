'''
esercizio
il computer pensa a un numero tra 0 e 9
tento di indovinarlo
se indovino il programma stampa un messaggio e termina
se non indovino devo riprovare a dare una nuova risposta
aggiunta di numero di tentativi massimo
aggiunta di suggerimenti
'''

import random

cpunum=0
cpunum=random.randint(1,90)
tentativi=(3)-1

print(cpunum)

LOOP=True
while LOOP:
    usernum=int(input(f'hai {tentativi+1} tentativi, indovina il numero: '))
    
    if (tentativi==0):
        print('game over tentativi esauriti')
        LOOP=False #potevo anche mettere break al posto di LOOP=False
        
    elif (cpunum==usernum):
        print(f'esatto ho pensato il num {cpunum} e hai indovinato con il num {usernum}')
        LOOP=False #potevo anche mettere break al posto di LOOP=False
        
    else:
        tentativi = tentativi-1
        print('sbagliato ritenta')
        
        if (usernum>cpunum):
            print(f'il numero che ho pensato è più piccolo')
            
        else:
            print(f'il numero che ho pensato è più grande')
        
        

        




