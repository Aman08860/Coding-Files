import random

while True:
    playerChoise = str(input('1:Rock , 2:Paper , 3:Scissor => '))
    
    if (playerChoise == 'exit'):
        break
    elif (playerChoise == '1'):
        playerChoise = 'Rock'
    elif (playerChoise == '2'):
        playerChoise = 'Paper'
    elif (playerChoise == '3'):
        playerChoise = 'Scissor'
    else:
        print('Please enter 1 or 2 or 3')
        
    botChoise = random.choice(['Rock', 'Paper', 'Scissor'])
    if (playerChoise == botChoise):
        print(playerChoise ,'vs', botChoise , "=> It's Draw ")
    elif (playerChoise == 'Rock' and botChoise == 'Scissor' or playerChoise == 'Paper' and botChoise == 'Rock' or playerChoise == 'Scissor' and botChoise == 'Paper'):
        print(playerChoise ,'vs', botChoise , "=> YOU WON")
    else:
        print(playerChoise ,'vs', botChoise , "=> BOT WON")