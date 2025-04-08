from gameFunctions import *
from gameAssets import *


def main():
    
    startGameFlag = getStartResponse()

    while startGameFlag == 'y':

        continuePlaying = True

        current_grid = initialGrid.copy()

        possibleChoices = [int(num) for num in possibleRange]

        while continuePlaying:

            display_grid(menu_grid, "Menu")

            display_grid(current_grid, "Current Grid")

            user_choice = getUserChoice()

            if user_choice in possibleChoices:

                userChoiceIndex = possibleChoices.index(user_choice)
                possibleChoices.pop(userChoiceIndex)

                current_grid = updateGrid(user_choice, current_grid, userSymbol)

                if len(possibleChoices) != 0:

                    computerChoice, possibleChoices = getComputerChoice(possibleChoices)

                    current_grid = updateGrid(computerChoice, current_grid, computerSymbol)

                continuePlaying, winner = check_for_winner(current_grid, possibleChoices)

        display_grid(current_grid, "Final Grid")
        announceWinner(winner)            

        startGameFlag = getStartResponse()

main()