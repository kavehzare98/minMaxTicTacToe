'''
GAME CLASS:
===========
ATTRIBUTES
    + possible_moves : list(string)

METHODS
    + get_default_grid : list(string)
    + get_menu_grid : list(string)
    + get_current_grid : list(string)
    + get_possible_moves : list(string)

    + set_default_grid(new_default : list(string) ) : void
    + set_menu_grid(new_menu : list(string) ) : void
    + set_current_grid(new_curr : list(string) ) : void
    + set_possible_moves(new_moves : list(string) ) : void

    + valid_move(move : int)  : bool
    + update_current_grid(move : int, symbol : string) : void
    + update_possible_moves(move : int) : void
    + is_draw() : bool
    + find_winner() : string

'''

class Game:
    def __init__(self):
        self.default_grid = ['-' for i in range(9)]
        self.menu_grid = [str(i) for i in range(1,10)]
        self.current_grid = self.default_grid
        self.possible_moves = self.menu_grid

    def 