import config as cf
from model import game, player
from view import cli_view as CLI


def main():

    o_game = game.Game()
    CLI.display_header()
    o_game.prompt_to_start()

    while o_game.get_start_flag():

        o_game = game.Game()
        o_player_1 = player.Player(cf.HUMAN_TYPE, cf.USER_SYMBOL)
        o_player_2 = player.Player()
        player_1_symbol =  o_player_1.get_player_symbol()
        player_2_symbol = o_player_2.get_player_symbol()

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

main()
