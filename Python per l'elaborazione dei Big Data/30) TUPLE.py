#tuple, liste i cui elementi non sono modificabili (diciamo in sola lettura)

frutta=('mela','pera','kiwi')

print(frutta)
for el in frutta:
    print(el,end=' ')
    
print('')

#frutta.append('fragola') ERROE! non posso aggiungere elementi a una tupla

#packing/unpackin
dati=('mela',100,1.98)
a,b,c=dati
print(a)
print(b)
print(c)

def calc(n,m):
    s=n+m
    p=n*m
    return s, p

somma, prodotto=calc(10,20)
print(somma)
print(prodotto)
