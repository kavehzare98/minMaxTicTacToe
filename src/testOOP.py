import config as cf
import game
import player


def main():

    oGame = game.Game()
    oGame.displayHeader()
    oGame.askToStartGame()

    while oGame.getStartFlag():

        oGame = game.Game()
        oUserPlayer = player.Player(cf.HUMAN_TYPE, cf.USER_SYMBOL)
        oComputerPlayer = player.Player()

        while oGame.checkForWinner(oUserPlayer, oComputerPlayer) != 'tie':
        
            # display grids (menu and current)
            gridChoice = oGame.getGrid("menu")
            oGame.displayGrid(gridChoice)
            
            gridChoice = oGame.getGrid("current")
            oGame.displayGrid(gridChoice)

            input1 = oUserPlayer.makeMove(oGame)

            if (oGame.checkMoveIsValid(input1) == True):
                oGame.updatePossibleMoves(input1)
                player_symbol = oUserPlayer.getPlayerSymbol()
                row, col = oGame.convertMoveToGridCoordinate(input1)
                coordinates = (row, col)
                oGame.updateCurrentGrid(coordinates, player_symbol)

                if oGame.checkForWinner(oUserPlayer, oComputerPlayer) != 'tie':
                    input2 = oComputerPlayer.makeMove(oGame)
                    oGame.updatePossibleMoves(input2)
                    player_symbol = oComputerPlayer.getPlayerSymbol()
                    row, col = oGame.convertMoveToGridCoordinate(input2)
                    coordinates = (row, col)
                    oGame.updateCurrentGrid(coordinates, player_symbol)

        # Prompt user whether to restart game
        oGame.askToStartGame()

    oGame.displayFooter()

main()