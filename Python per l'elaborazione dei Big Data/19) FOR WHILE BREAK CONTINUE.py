print('for da 0 a 9')

for i in range(10):
    print(i,end=' ')

print('\n')
#for con  break
for i in range(10):
    print(i,end=' ')
    if(i==5):
        break #interrompe il ciclo forzandolo

print('\n')
#for con  continue
for i in range(10):
    if(i==5):
        continue #continua il ciclo
    print(i,end=' ')
    
print('\n')
#while con break
n=0
while(n<10):
    n +=1 #incrementa n di uno
    if(n==5):
        break
    print(n,end=' ')
    
print('\n')
#while con continue
n=0
while(n<10):
    n +=1 #incrementa n di uno
    if(n==5):
        continue
    print(n,end=' ')