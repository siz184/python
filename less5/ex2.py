positions = [
    '-','-','-', #1,2,3
    '-','-','-', #4,5,6
    '-','-','-'  #7,8,9
]
signs = ['-','x','o']
turn = 1

def checkWin(positions,sign):
    check=0
    a=0
    b=3
    for i in range(a,b):
        if positions[i]==sign:
            check+=1


def checkEnd(positions):
    if '-' in positions:
        return 0
    else:
        return 1

def checkFill(positions,pos):
    if positions[pos]=='-':
        return 0
    else:
        return 1

def oneTurn(positions,turn):
    player = int(input(f"Player {turn}: "))
    if 0 < player > 9:
        print ("Fill 1 - 9")
    elif checkFill(positions,player - 1):
        print (f"Position {player} is filled")
    else:
        positions[player - 1] = signs[turn]
        turn += 1
        turn = 1 if turn > 2 else 2
    return positions,turn

def createTable(positions):
    row = ''
    for i in range(0,len(positions)):
        p = i+1
        row += positions[i] + ' '
        if p%3==0 :
            print(f"{row}")
            row = ''

while checkEnd(positions) != 1:
    positions,turn = oneTurn(positions,turn)
    createTable(positions)
        
    
    

print(f"Player {turn} win!")