'''
calcolo la media di 5 numeri usando una lista
'''
voti=[]

for n in range(5):
    print(f'voto n.{n+1}) - ', end=' ')
    voto=int(input('voto: '))
    voti.append(voto)

somma=0
for n in voti:
    #print(n)
    somma=somma+n
    #oppure si può usare la forma compatta
    #somma +=n
    
    
print("somma: ",somma)

media=somma/len(voti)
print("media: ",media)