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

print('numeri pari')
for el in listanumpari:
    print(el)

print('numeri dispari')
for el in listanumdispari:
    print(el)

#ordinamento lista al contrario metodo 1 -1-i
print('metodo 1')
for i in range(len(listanumpari)):
    indice=len(listanumpari)-1-i;
    print(listanumpari[indice], end=' ')

#ordinamento lista al contrario metodo 2 indice
print('\nmetodo 2')
for i in range(len(listanumpari), 0, -1):
    indice = i-1;
    print(listanumpari[indice], end=" ")

#ordinamento lista al contrario metodo 3 reversed
print('\nmetodo 3')
for i in reversed(listanumpari):
    print(i, end=" ")
    
#ordinamento lista al contrario metodo 3 slicing
print('\nmetodo 4')
for i in listanumpari[::-1]:
    print(i, end=" ")


