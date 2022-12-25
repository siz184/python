positions = [
    '-','-','-', #1,2,3 for users / 0,1,2
    '-','-','-', #4,5,6 for users / 3,4,5
    '-','-','-'  #7,8,9 for users / 6,7,8
]

# positions = [
#     '-','-','-','-', #1,2,3,4 for users     / 0,1,2,3
#     '-','-','-','-', #5,6,7,8 for users     / 4,5,6,7
#     '-','-','-','-', #9,10,11,12 for users  / 8,9,10,11
#     '-','-','-','-'  #13,14,15,16 for users / 12,13,14,15
# ]
# c = 4

winner = 0
signs = ['-','x','o']
turn = 1
c = 3

def checkWin(positions,sign):
    check=0
    a=0
    b=c
    for i in range(c):
        check = 0
        for j in range(a,b):
            if positions[j]==sign:
                check+=1
            if check==c:
                return 1    
        a+=c
        b+=c

    a=0
    b=c**2-c+1
    for i in range(c):
        check = 0
        for j in range(a,b,c):
            if positions[j]==sign:
                check+=1
            if check==c:
                return 1  
        a+=1
        b+=1

    check = 0
    for i in range(0,c**2,c+1):
        if positions[i]==sign:
            check+=1
        if check==c:
            return 1

    check = 0
    for i in range(c-1,c**2-c+1,c-1):
        if positions[i]==sign:
            check+=1
        if check==c:
            return 1 

    return 0


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
    if 0 < player > c**2:
        print ("Fill 1 - 9")
    elif checkFill(positions,player - 1):
        print (f"Position {player} is filled")
    else:
        positions[player - 1] = signs[turn]
        if checkWin(positions,signs[turn]):
            return positions,turn,1
        else:    
            turn += 1
            turn = 1 if turn > 2 else 2
    return positions,turn,0

def createTable(positions):
    row = ''
    for i in range(0,len(positions)):
        p = i+1
        row += positions[i] + ' '
        if p%c==0 :
            print(f"{row}")
            row = ''

while checkEnd(positions) != 1:
    if winner==1:
        break
    else:
        positions,turn,winner = oneTurn(positions,turn)
        createTable(positions)
    
    
if winner==1:
    print(f"Player {turn} win!")
else:
    print("Draw!")