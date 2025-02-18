from gameFunctions import *
from gameAssets import *


def main():
    
    startGameFlag = getStartResponse()

    while startGameFlag == 'y':

        continuePlaying = True

        currentGrid = initialGrid.copy()

        possibleChoices = [int(num) for num in possibleRange]

        while continuePlaying:

            displayGrid(menuGrid, "Menu")

            displayGrid(currentGrid, "Current Grid")

            userChoice = getUserChoice()

            if userChoice in possibleChoices:

                userChoiceIndex = possibleChoices.index(userChoice)
                possibleChoices.pop(userChoiceIndex)

                currentGrid = updateGrid(userChoice, currentGrid, userSymbol)

                if len(possibleChoices) != 0:

                    computerChoice, possibleChoices = getComputerChoice(possibleChoices)

                    currentGrid = updateGrid(computerChoice, currentGrid, computerSymbol)

                continuePlaying, winner = checkForWinner(currentGrid, possibleChoices)

        displayGrid(currentGrid, "Final Grid")
        announceWinner(winner)            

        startGameFlag = getStartResponse()

main()