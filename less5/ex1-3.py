import random

candy = 123
turn = 1
turnList = [candy,turn]

def oneTurn(candy,turn):
    if turn == 1:
        player = int(input(f"Player {turn}: "))
    else:
        if candy > 28*2:
            player = random.randint(1,28)
        elif candy > 28:
            player = candy - 29
        else:
            player = candy
        print(f"Player 2: {player}")
    if 1 < player > 28:
        print ("Fill 1 - 28")
    elif player > candy:
        print (f"Fill 1-{candy}")
    else:
        candy -= player
        if candy > 0:
            turn += 1
            turn = 1 if turn > 2 else 2
    turnList = [candy,turn]
    return turnList


while turnList[0] > 0:
    print(f"Candy: {turnList[0]}")
    turnList = oneTurn(turnList[0],turnList[1])

print(f"Player {turnList[1]} win!")