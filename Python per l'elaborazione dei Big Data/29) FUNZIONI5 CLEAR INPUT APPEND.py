'''
text editor in python
-riceve una riga di testo per volta
-memorizza le righe di testo in una lista
-visualizza il testo
-posso eliminare una riga di testo

extra
-inserisco una riga di testo in una posizione a piacere
'''
righe=[] #creo lista vuota per le righe dove farò l append

def EditorHelp():
    print('h - help')
    print('i - inserisce una linea')
    print('c - cancella il buffer')
    print('p - stampa il buffer')
    print('q - stampa il buffer')

def InsertLine():
    linea=input('>')
    righe.append(linea)
    
def PrintText():
    for l in righe:
        print(l)
        
def ClearText():
       righe.clear() #.clear svuota il contenuto delle righe
    
EditorHelp()
while (True):
    cmd=input('comando? ') #risposta di input dentro variabile cmd
    if not cmd:
        break;
    elif(cmd=='h'): #visualizzazione help
        EditorHelp()    
    elif(cmd=='i'): #inserire una linea
        InsertLine()
    elif(cmd=='p'): #stampa il testo completo
        PrintText()
    elif(cmd=='c'): #svuota il testo
        ClearText()
    elif(cmd=='q'): #svuota il testo
        break;
    
        