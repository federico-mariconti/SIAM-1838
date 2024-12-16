def saluta():
    #corpo della funzione
    print ('ciao')

saluta()

def SalutaConNome(nome):
    #funzione con un parametro
    print('ciao', nome)

def somma(a,b):
    #funzione con due parametri che restituisce un risultato
    s=a+b
    return s

saluta()
SalutaConNome('Mario')

x=somma(10,20)
print(x)

def ElaboraNumeri(numeri):
    #funzione che riceve un parametro lista
    for el in numeri:
        print(el, end=' ')

num=[1,2,3,4,5]
ElaboraNumeri(num)