'''
esercizio
programma per la lista della spesa
-chiedo quante cose ci sono da comprare
-metto gli oggetti in una lista
-stampo gli oggetti uno a uno
'''
print('Lista della spesa')

oggetti=[] #creo lista vuota
quantita=int(input('quanti oggetti devono essere comprati? '))

#chiedo oggetti da mettere nella lista
for i in range(quantita):
    oggetto=input(f'oggetto n.{i+1} --> ')
    oggetti.append(oggetto)

print('grazie')
input('premi INVIO per stampare la lista')

#stampa la lista della spesa
print('\nLista della spesa')
conta=1
for el in oggetti:
    print(f'{conta}. {el}')
    conta +=1
