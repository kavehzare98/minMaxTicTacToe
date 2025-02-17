from src.gameAssets import *
from random import choice

def getStartResponse():

    """
    This function takes input from the user, converts it to lower case, 
    extracts and returns the first letter of the user's response.
    """

    print("Would you like to play (Yes or No)?\n")
    
    userInput = input("Please make a choice:\t")

    firstLetterOfResponse = userInput.lower()[0]

    return firstLetterOfResponse


def displayGrid(grid, gridName):
    """
    This functions displays a grid input which is a dictionary.
    It displays the dictionary with some formatting in a 3x3 orientation
    """
    print(f"{gridName}:\n")
    key = 1
    for i in range(2):
        keys = list(range(key, key + 3))
        print(f"  {grid[keys[0]]} | {grid[keys[1]]} | {grid[keys[2]]}")
        print(gridLine)
        key += 3

    # Print final row of values
    keys = list(range(key, key + 3))
    print(f"  {grid[keys[0]]} | {grid[keys[1]]} | {grid[keys[2]]}", end="\n\n")

    # End of function defintion

def getUserChoice():
    print("\n")
    userChoice = input("Please choose an empty ('-') square:\t")
    print("\n")

    while userChoice not in possibleRange:
        
        userChoice = input("Invalid Input! Please choose an empty ('-') square between 1 to 9:\t")

    userChoice = int(userChoice)

    return userChoice


def updateGrid(choice, currentState, symbol):
    """
    This function updates the current state (grid)
    and returns the current state (since there is no pass by reference).
    """
    currentState[choice] = symbol

    return currentState


def getComputerChoice(possibleChoices):

    """
    This function takes an input which is a list of all possible choices. Updates that list and
    returns 2 items: the actual choice as well as the list of possible choices.
    """

    computerChoice = choice(possibleChoices)
    choiceIndex = possibleChoices.index(computerChoice)
    possibleChoices.pop(choiceIndex)

    return computerChoice, possibleChoices


def checkForWinner(currentState, possibleChoices):
    
    if len(possibleChoices) == 7:
        continueFlag = True
        winner = None
    else:
        if (currentState[1] == currentState[2] == currentState[3]) and (currentState[1] != '-'):
            continueFlag = False
            winner = currentState[1]
        elif (currentState[4] == currentState[5] == currentState[6]) and (currentState[4] != '-'):
            continueFlag = False
            winner = currentState[4]
        elif (currentState[7] == currentState[8] == currentState[9]) and (currentState[7] != '-'):
            continueFlag = False
            winner = currentState[7]
        elif (currentState[1] == currentState[4] == currentState[7]) and (currentState[1] != '-'):
            continueFlag = False
            winner = currentState[1]
        elif (currentState[2] == currentState[5] == currentState[8]) and (currentState[2] != '-'):
            continueFlag = False
            winner = currentState[2]
        elif (currentState[3] == currentState[6] == currentState[9]) and (currentState[3] != '-'):
            continueFlag = False
            winner = currentState[3]
        elif (currentState[1] == currentState[5] == currentState[9]) and (currentState[5] != '-'):
            continueFlag = False
            winner = currentState[5]
        elif (currentState[3] == currentState[5] == currentState[7]) and (currentState[5] != '-'):
            continueFlag = False
            winner = currentState[5]
        elif len(possibleChoices) == 0:
            continueFlag = False
            winner = "Tie"
        else:
            continueFlag = True
            winner = None
    
    return continueFlag, winner


def announceWinner(winner):
    if winner == userSymbol:
        print("The winner is:\tUSER")
    elif winner == userSymbol:
        print("The winner is:\tCOMPUTER")
    else:
        print("It's a TIE!")