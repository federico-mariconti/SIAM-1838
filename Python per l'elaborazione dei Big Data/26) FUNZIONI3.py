#una funzione non potrà mai cambiare il valore di una variabile perchè lavora sempre su una copia
def CambiaNome(n):
    n='Mario'
    print('f',n)
    
def CambiaNome2(n):
    n='Mario'
    print('f',n)
    return n

nome='Luigi'

print('1',nome)
CambiaNome(nome)
print('2',nome)

print('3',nome)
CambiaNome2(nome)
print('4',nome)