import config as cf
import player

class Game():
    def __init__(self, startFlag=False, gameMode=cf.SINGLE_PLAYER_MODE):
        """
        Constructor for Game class.

        Parameters:
        startFlag (bool): flag to determine if game should start (default=False)
        gameMode (str): specifies single player or multiplayer mode (default=cf.SINGLE_PLAYER_MODE)

        Sets up game attributes, including start flag, default grid, current grid,
        menu grid, possible moves, and game mode.
        """
        self.startFlag = startFlag
        self.defaultGrid = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        self.currentGrid = self.defaultGrid
        self.menuGrid = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
        self.possibleMoves = [str(num) for num in range(1, 10)]
        self.mode = gameMode

    def displayHeader(self):
        print("""=======================
WELCOME TO TIC TAC TOE!
=======================
            """)
    
    def displayFooter(self):
        print("""========
BYE BYE!
========
            """)

    def askToStartGame(self):
        """
        Prompts the user to start the game.

        Asks the user if they would like to play the game and sets the start 
        flag to True if the response begins with y. Does not return the flag.

        Returns:
            bool: True if the game should start, False otherwise.
        """
        startGamePrompt = input("Would you like to play? ")
        startGameFlag = startGamePrompt.lower()[0]
        if startGameFlag == 'y':
            self.startFlag = True
        else:
            self.startFlag = False


    def getStartFlag(self):
        return self.startFlag
    
    def setGameMode(self):

        """
        Prompts the user to select a game mode.

        Displays the available game modes (Single Player or Multiplayer) and 
        prompts the user to enter a choice. Continues to prompt until a valid 
        choice is made. Sets the game's mode based on the user's selection.

        Updates:
            self.mode (str): The selected game mode, either SINGLE_PLAYER_MODE 
            or MULTIPLAYER_MODE.
        """

        print("""Choose one of the following game modes:
    1. Single Player
    2. Multiplayer
        """)

        modeChoices = [cf.SINGLE_PLAYER_MODE, cf.MULTIPLAYER_MODE]

        userChoice = input("Enter your choice:\t")

        while userChoice not in modeChoices:
            userChoice = input("Invalid choice! Enter your choice (1 or 2):\t")


        self.mode = userChoice

    def checkMoveIsValid(self, moveStr):

        """
        Checks if a move is valid or not.

        Parameters:
            moveStr (str): Move to be checked

        Returns:
            bool: True if the move is valid, False otherwise

        A move is valid if it is in the list of possible moves.
        """
        validFlag = True

        if moveStr not in self.possibleMoves:
            validFlag = False

        return validFlag
    
    def convertMoveToGridCoordinate(self, moveStr):
        moveNumber = int(moveStr)
        moveIndex = moveNumber - 1

        if moveIndex < 3:
            # Row 1
            rowIndex = 0
        elif moveIndex < 6:
            # Row 2
            rowIndex = 1
        else:
            # Row 3
            rowIndex = 2
        
        columnIndex = moveIndex % 3

        return rowIndex, columnIndex
    
    def updateCurrentGrid(self, moveCoordinates, symbol):
        if symbol:
            row = moveCoordinates[0]
            column = moveCoordinates[1]
            self.currentGrid[row][column] = symbol

    def updatePossibleMoves(self, moveStr):
        removeIndex = self.possibleMoves.index(moveStr)
        self.possibleMoves.pop(removeIndex)

    def getGrid(self, gridSpecifier):
        """
        Returns a grid based on the specifier.

        Parameters:
        gridSpecifier (str): a string that specifies the type of grid to return.
            "menu" returns the menu grid, while "current" returns the current grid.

        Returns:
        list: a 2D list of strings representing the grid.
        """
        if gridSpecifier == "menu":
            return self.menuGrid
        elif gridSpecifier == "current":
            return self.currentGrid

    def displayGrid(self, grid):
        print()
        col = 0
        for row in range(3):
            print(f" {grid[row][col]} | {grid[row][col + 1]} | {grid[row][col + 2]}")
            if row != 2:
                print("---+---+---")
        print()

    def checkForWinner(self, player1, player2):
        if len(self.possibleMoves) == 0:
            return "tie"
        
    def getPossibleMoves(self):
        return self.possibleMoves
