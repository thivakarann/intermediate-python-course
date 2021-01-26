import random

def main():
    player1=0
    player1wins=0
    player2=0
    player2wins=0
    rounds=1

    while rounds !=4:
        print("Rounds"+str(rounds))
        player1 =dice_roll()
        player2 =dice_roll()
        print ("player 1 roll:" + str(player1))
        print ("player 1 roll:" + str(player2))
        if player1==player2:
            print("Draw")
        elif player1>player2:
            player1wins+=1
            print("Player 1 wins")
        else:
            player2wins+=1
            print("Player 2 wins")
        rounds +=1
    if player1wins==player2wins:
        print("Draw")
    elif player1wins>player2wins:
        print("Player 1 wins - rounds won:"+str(player1wins))
    else:
        print("Player 2 wins - rounds won:"+str(player2wins))
        
        
def dice_roll():
    diceRoll=random.randint(1,6)
    return diceRoll

main()
