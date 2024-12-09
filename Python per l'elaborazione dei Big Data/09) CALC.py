'''
scrivere un programma per eseguire calcoli che chieda 2 numeri e che operazione svolgere e quindi calcoli il risultato

chiedo il primo numero
chiedo il secondo numero
chiedo che operazione svolgere

calcolo il risultato
'''

print("calcolatrice")
print("Inserire due numeri e l'operazione desiderata")
n1=int(input("numero 1= :"))
n2=int(input("numero 2= :"))
op=input("operazione (+,-,x,:): ")

#risultato del calcolo

res = 0

if(op=="+"):
    res=n1+n2
elif(op=="-"):
    res=n1-n2
elif(op=="x"):
    res=n1*n2
elif(op==":"):
    if(n2==0):
        res=0;
        print("errore divisione per 0")
        ERRORE=True
    else:
        res=n1/n2
else:
    print("?")
    op="?"
    ERRORE=True
    
if (not ERRORE):
#print("res=", res)
    print(f"{n1} {op} {n2} = {res}")
else:
    print("Errore: verifica i dati inseriti!")
    