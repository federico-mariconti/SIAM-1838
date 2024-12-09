'''
Programma pari e dispari

Chiedo quanti numeri elaborare
mi faccio dare i numeri, uno alla volta
verifico se il numero è pari o dispari
se è pari lo aggiungo a una lista
stampo i numeri pari

come capisco se un numero è pari o dispari?
Uso l operatore modulo % (diviso)
10 % 2 = 0
11 % 2 = 1
2 % 2 = 0
3 % 2 = 1

se il risultato di modulo è 0 allora il numero è pari
altrimenti è dispari
'''

listanumpari=[]
listanumdispari=[]
quantita=int(input('quanti numeri devo elaborare? '))

print(quantita)

for el in range(quantita):
    numero=int(input(f'numero {el+1} ---> '))
    if ((numero % 2) == 0):
        print('il numero è pari')
        listanumpari.append(numero)
    else:
        print('il numero non è pari')
        listanumdispari.append(numero)

print('numeri pari',listanumpari, end=' ')
print('\n', 'numeri dispari', listanumdispari, end=' ')

print('numeri pari',listanumpari(-1), end=' ')
print('\n', 'numeri dispari', listanumdispari(-1), end=' ')
