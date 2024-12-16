def StampaPersone(*persone):
    #...
    print('numero di parametri:',len(persone))
    for p in persone:
        print(p, end=' ')

StampaPersone('Mario')
StampaPersone('Mario','Luigi','Anna')
print('\n')

def AssettoDrone(pitch, roll, yaw):
    print(f'pitch: {pitch}, roll: {roll}, yaw: {yaw}')

AssettoDrone(12,0,90)
AssettoDrone(yaw=90, roll=23, pitch=56) #posso specificare i campi in modo tale da non dover rispettare l ordine)

def AssettoDrone2(pitch=90, roll=0, yaw=180):
    print(f'pitch: {pitch}, roll: {roll}, yaw: {yaw}')
    
AssettoDrone2(yaw=90)