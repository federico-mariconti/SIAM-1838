#insiemi
s1={2,4,6,8,10}
print('s1',s1,type(s1))  #type restituisce il tipo degli elementi

lista=[2,2,2,3,4,5,5,6,7,1]
s2=set(lista) #set crea un insieme, un insieme rimuove i duplicati, non è detto che nell insieme gli elementi siano ordinati
print('s2',s2)

s3=set()
s3.add('mela') #aggiunge elementi
s3.add('banana')
s3.add('fragola')
print('s3',s3)

s3.discard('banana')
print('s3',s3)

if 'fragola' in s3:
    print('fragola ok')
    
#scorro gli elementi con for, l ordine non è garantito

for n in s1:
    print(n, end=' ')
print('') #va a capo dopo aver stampato la lista

a={1,2,3,10,20}
b={10,20,30,40,50}

c= a.union(b) #unione dei due insiemi, vedrò tutti gli elementi dei due insiemi
print('union', c)

c=a.intersection(b) #intersezione dei due insiemi, vedrò solo gli elementi in comune tra i due insiemi
print('intersection', c)

c=a.difference(b) #differenza tra i due insiemi, vedrò solo gli insiemi non in comune di A
print('difference A',c)

c=b.difference(a) #differenza tra i due insiemi, vedrò solo gli insiemi non in comune di B
print('difference B',c)
