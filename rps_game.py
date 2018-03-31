#!/usr/bin/env python

import random

def getUserChoice(maxInvalidChoices=3):
    # By default user will be given 3 tries to enter a valid choice.
    # the choice should be r for Rock, p for Paper or s for sissors
    while(maxInvalidChoices > 0):
        userChoice = raw_input('Enter your choice (use r for Rock, p for paper or s for scissors): ')

        if userChoice in ('r', 'p', 's'):
            return userChoice
        else:
            print('Invalid choice. Try again')
            maxInvalidChoices -=1
    print('Reached maximum number of invalid choices. Restart game to play again')
    return None

def getComputerChoice():
    allPossibleValues = ('r', 'p', 's')
    computerChoice = random.choice(allPossibleValues)
    return computerChoice

def playGame():
    print('##############################################')
    print('       Rock, Paper, Sissors Game!!!')
    print('##############################################')

    abvToFullName = {'r': 'Rock', 'p' : 'Paper', 's': 'Scissors'}
    gameScore = {'Total Games' : 0, 'User Wins':0, 'Computer Wins': 0, 'Draws': 0}

    while(1):
        userChoice = getUserChoice()
        print('User entered: ' + abvToFullName.get(userChoice))

        computerChoice = getComputerChoice()
        print('Computer entered: ' + abvToFullName.get(computerChoice))

        drawCount = gameScore['Draws']
        userWins = gameScore['User Wins']
        computerWins = gameScore['Computer Wins']

        if userChoice == computerChoice:
            print('Draw')
            gameScore['Draws'] = drawCount + 1
        elif userChoice == 'r':
            if computerChoice == 'p':
                print('Computer wins: ' + abvToFullName.get(computerChoice) + ' wraps ' + abvToFullName.get(userChoice))
                gameScore['Computer Wins'] = computerWins + 1
            else:
                print('User wins: '+ abvToFullName.get(userChoice)+ ' breaks '+ abvToFullName.get(computerChoice))
                gameScore['User Wins'] = userWins + 1
        elif userChoice == 'p':
            if computerChoice == 'r':
                print('User wins: '+ abvToFullName.get(userChoice)+ ' wraps '+ abvToFullName.get(computerChoice))
                gameScore['User Wins'] = userWins + 1
            else:
                print('Computer wins: '+ abvToFullName.get(computerChoice)+ ' cut '+ abvToFullName.get(userChoice))
                gameScore['Computer Wins'] = computerWins + 1
        elif userChoice == 's':
            if computerChoice == 'r':
                print('Computer wins: '+ abvToFullName.get(computerChoice)+ ' breaks '+ abvToFullName.get(userChoice))
                gameScore['Computer Wins'] = computerWins + 1
            else:
                print('User wins: '+ abvToFullName.get(userChoice)+ ' cut '+ abvToFullName.get(computerChoice))
                gameScore['User Wins'] = userWins + 1

        totalGames = gameScore['Total Games']
        gameScore['Total Games'] = totalGames + 1

        checkToContinue = raw_input('Do you want to continue playing (use y for Yes, n for No: ')
        if checkToContinue == 'y':
            continue
        else:
            break

    # print final score
    print('Total Games played: '+ str(gameScore['Total Games']))
    print('User Wins: '+ str(gameScore['User Wins']))
    print('Computer Wins: '+ str(gameScore['Computer Wins']))
    print('Draws: '+ str(gameScore['Draws']))

def main():
    playGame()

if __name__ == "__main__":
    main()
