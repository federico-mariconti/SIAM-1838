numeri=[12,23,34,45,56,67]
print(numeri)
print("primo elemento", numeri[0])
print("secondo elemento", numeri[1])
print("terzo elemento", numeri[2])

#per sapere il numero di elementi di una lista uso len
print("numero di elementi",len(numeri))

indice=0
print("elemento:", numeri[indice])
indice+=1
print("elemento:", numeri[indice])
indice+=1
print("elemento:", numeri[indice])

numeri[0]=99
print(numeri)

dati=[123,"mele",1.98,100]
print(dati)

amici=[]
cugini=list()

#per aggiungere un elemento utilizzo .append, permette l aggiunta di un solo elemento
amici.append("Mario")
amici.append("Luigi")
amici.append("Anna")
print(amici)

#per inserire in una certa posizione utilizzo .insert
amici.insert(1,"Demetrio")
print(amici)

#per rimuovere un certo elemento utilizzo .remove
amici.remove("Demetrio")
print(amici)

print("\n", numeri, sep="")
numeri.extend([100,200,300]) #utilizzo .extend per aggiungere piu di un elemento
print(numeri)

numeri.pop() #.pop toglie, se non specificato, l ultimo elemento
print(numeri)
numeri.pop(1) #.pop(1) in questo caso è specificata la posizione dell elemento da togliere
print(numeri)
numeri.remove(99)
print(numeri)

print(numeri[-1]) #con indice negativi parto a contare le posizioni dal fondo
#slicing di seguito
print(numeri[2:4]) #in questo caso mi restituisce gli elementi da posizione 2 a 4 (esclusa la pos 4)
print(numeri[:4]) #in questo caso restituisce tutti gli elementi dall inizio fino alla posizione 4 esclusa
print(numeri[2:]) #in questo restituisce tutti gli elementi a partire dalla posizione 2 compresa

if(100 in numeri):
    print("presente")
    