'''
GAME CLASS:
    + update_current_grid(move : int, symbol : string) : void
    + update_possible_moves(move : int) : void
    + is_draw() : bool
    + find_winner() : string
    + reset_game() : void

'''

class Game:
    def __init__(self):
        self.default_grid = ['-' for i in range(9)]
        self.menu_grid = [str(i) for i in range(1,10)]
        self.current_grid = self.default_grid
        self.possible_moves = self.menu_grid

    # GETTERS
    def get_default_grid(self) -> list:
        return self.default_grid
    
    def get_menu_grid(self) -> list:
        return self.menu_grid
    
    def get_current_grid(self) -> list:
        return self.current_grid
    
    def get_default_grid(self) -> list:
        return self.possible_moves
    
    # SETTERS
    def set_default_grid(self, new_grid : list) -> None:
        self.default_grid = new_grid

    def set_menu_grid(self, new_grid : list) -> None:
        self.menu_grid = new_grid

    def set_current_grid(self, new_grid : list) -> None:
        self.current_grid = new_grid
        
    def set_possible_moves(self, new_moves : list) -> None:
        self.possible_moves = new_moves

    # SPECIAL METHODS
    def validate_move(self, move : int) -> bool:
        if move in self.possible_moves:
            return True
        return False
    
    def update_current_grid(move : int, symbol : string) : void