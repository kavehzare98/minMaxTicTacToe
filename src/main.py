import config as cf
from model import game, player
from view import cli_view as CLI


def main():

    oGame = game.Game()
    CLI.display_header()
    oGame.prompt_to_start()

    while oGame.get_start_flag():

        oGame = game.Game()
        oPlayer1 = player.Player(cf.HUMAN_TYPE, cf.USER_SYMBOL)
        oPlayer2 = player.Player()
        player1Symbol =  oPlayer1.getPlayerSymbol()
        player2Symbol = oPlayer2.getPlayerSymbol()

        while oGame.get_game_over_status() == False:
        
            # display grids (menu and current)
            oGame.display_grid(oGame.get_menu_grid())
            oGame.display_grid(oGame.get_current_grid())

            input1 = oPlayer1.makeMove(oGame)

            if (oGame.is_valid_move(input1) == True):
                oGame.update_possible_moves(input1)
                row, col = oGame.convert_move_to_coordinate(input1)
                coordinates = (row, col)
                oGame.update_current_grid(coordinates, player1Symbol)
                oGame.check_for_winner(player1Symbol, player2Symbol)

                if oGame.get_game_over_status() == False:
                    input2 = oPlayer2.makeMove(oGame)
                    oGame.update_possible_moves(input2)
                    row, col = oGame.convert_move_to_coordinate(input2)
                    coordinates = (row, col)
                    oGame.update_current_grid(coordinates, player2Symbol)
                    oGame.check_for_winner(player1Symbol, player2Symbol)
        
        oGame.display_grid(oGame.get_current_grid())
        print(f"The Winner of the Game is: {oGame.get_winner()}")

        # Prompt user whether to restart game
        oGame.prompt_to_start()

    CLI.display_footer()

main()
