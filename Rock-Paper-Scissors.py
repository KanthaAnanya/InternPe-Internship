from random import randint
#moves for the player
moves=['rock','paper','scissors']

while True:
    computer=moves[randint(0,2)] #computer takes moves as random integer from 0 to 2 i.e index values of moves
    player=input('rock,paper or cissors? (or end the game)').lower()
    if player =='end the game':
        print('THE GAME HAS ENDED.')
        break
    elif player==computer:
        print('Tie!!')
    elif player=='rock':
        if computer=='paper':
            print('You Loose',computer,'beats',player)
        else:
            print('You won!!',player ,'beats',computer)
    elif player=='paper':
        if computer=='scissorss':
            print('You Loose',computer,'beats',player)
        else:
            print('You won!!',player ,'beats',computer)
    elif player=='scissors':
        if computer=='rock':
            print('You Loose',computer,'beats',player)
        else:
            print('You won!!',player ,'beats',computer)
    else:
        print('check the spelling and try again')
