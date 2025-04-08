import config as cf
import game
import player


def main():

    oGame = game.Game()
    oGame.displayHeader()
    oGame.askToStartGame()

    while oGame.getStartFlag():

        oGame = game.Game()
        oPlayer1 = player.Player(cf.HUMAN_TYPE, cf.USER_SYMBOL)
        oPlayer2 = player.Player()
        player1Symbol =  oPlayer1.getPlayerSymbol()
        player2Symbol = oPlayer2.getPlayerSymbol()

        while oGame.getGameOver() == False:
        
            # display grids (menu and current)
            oGame.displayGrid(oGame.getMenuGrid())
            oGame.displayGrid(oGame.getCurrentGrid())

            input1 = oPlayer1.makeMove(oGame)

            if (oGame.checkMoveIsValid(input1) == True):
                oGame.updatePossibleMoves(input1)
                row, col = oGame.convertMoveToGridCoordinate(input1)
                coordinates = (row, col)
                oGame.updateCurrentGrid(coordinates, player1Symbol)
                oGame.checkForWinner(player1Symbol, player2Symbol)

                if oGame.getGameOver() == False:
                    input2 = oPlayer2.makeMove(oGame)
                    oGame.updatePossibleMoves(input2)
                    row, col = oGame.convertMoveToGridCoordinate(input2)
                    coordinates = (row, col)
                    oGame.updateCurrentGrid(coordinates, player2Symbol)
                    oGame.checkForWinner(player1Symbol, player2Symbol)
        
        oGame.displayGrid(oGame.getCurrentGrid())
        print(f"The Winner of the Game is: {oGame.getWinner()}")

        # Prompt user whether to restart game
        oGame.askToStartGame()

    oGame.displayFooter()

main()
