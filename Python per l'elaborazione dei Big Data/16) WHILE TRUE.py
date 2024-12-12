LOOP = True

while(LOOP):
    a=int(input('A: '))
    b=int(input('B: '))
    print(f'{a}+{b}={(a+b)}')
    
    answer=input('ancora (s/n)?: ')
    if answer != 's':
        LOOP=False
        