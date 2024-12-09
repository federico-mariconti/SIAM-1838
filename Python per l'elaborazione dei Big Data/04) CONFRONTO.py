print("confronto due numeri")
a=int(input("primo numero: "))
b=int(input("secondo numero: "))
c=int(input("terzo numero: "))

if(a<b):
    if(b>c):
        print(f"{b}; il secondo numero è il maggiore")
    else:
        print(f"{c}; il terzo numero è il maggiore")
elif (a<c):
    print(f"{c}; il terzo numero è il maggiore")
else:
    print(f"{a}; il primo numero è il maggiore")
