#le funzioni con le liste si comportano diversamente
def CambiaLista(lista):
    lista[0]=99
    
numeri=[1,2,3,4]

print(numeri)
CambiaLista(numeri)
print(numeri)