#dizionari
listino={'mele':12,'pere':23,'kiwi':45}
print(listino, type(listino))

print(listino['mele']) #estrarre il valore di un elemento

listino['mele']=99 #modificare
print(listino)

listino['fragole']=56 #aggiungere
print(listino)

listino.pop('fragole') #togliere
print(listino)

d1=dict() #dictionary vuoto

for el in listino.keys():
    print(el,end=' ')
print('')

for el in listino.values():
    print(el, end=' ')
print('')

for el in listino.items():
    print(el, el[0], el[1])

if 'mele' in listino:
    print('trovato mele')

listino2=listino
print(listino)
print(listino2)
listino['mele']=0
print(listino)
print(listino2)

listino3=listino.copy()
print(listino)
print(listino3)
listino['mele']=100
print(listino)
print(listino3)