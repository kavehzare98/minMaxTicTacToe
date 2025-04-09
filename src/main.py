import config as cf
from model import game, player
from view import cli_view as CLI


def main():

    # initialize an object of Game class
    o_game = game.Game()

    # view: show CLI header
    CLI.display_header()

    # view: prompt user to start game
    o_game.prompt_to_start()

    # controller: game loop start after validation
    while o_game.get_start_flag():

        # Reinitializing game for the new round, but repeating myself here
        o_game = game.Game()

        # creating two instances of Player class, could be asking user for multiplayer and level here
        o_player_1 = player.Player(cf.HUMAN_TYPE, cf.USER_SYMBOL, difficulty=1)
        o_player_2 = player.Player(cf.COMPUTER_TYPE, cf.COMPUTER_SYMBOL, difficulty=1)

        # getting player symbol instead of setting it
        player_1_symbol =  o_player_1.get_player_symbol()
        player_2_symbol = o_player_2.get_player_symbol()

        # while game is not over
        while o_game.get_game_over_status() == False:
        
            # display grids (menu and current)
            o_game.display_grid(o_game.get_menu_grid())
            o_game.display_grid(o_game.get_current_grid())


            input_1 = o_player_1.make_move(o_game)

            if (o_game.is_valid_move(input_1) == True):
                o_game.update_possible_moves(input_1)
                coordinate = o_game.convert_move_to_coordinate(input_1)
                o_game.update_current_grid(coordinate, player_1_symbol)
                o_game.check_for_winner(player_1_symbol, player_2_symbol)

                if o_game.get_game_over_status() == False:
                    input_2 = o_player_2.make_move(o_game)
                    o_game.update_possible_moves(input_2)
                    coordinate = o_game.convert_move_to_coordinate(input_2)
                    o_game.update_current_grid(coordinate, player_2_symbol)
                    o_game.check_for_winner(player_1_symbol, player_2_symbol)
        
        o_game.display_grid(o_game.get_current_grid())
        print(f"The Winner of the Game is: {o_game.get_winner()}")

        # Prompt user whether to restart game
        o_game.prompt_to_start()

    CLI.display_footer()


if __name__ == "__main__":
    main()