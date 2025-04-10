import config as cf
from model import player

class Game():
    def __init__(self):
        """
        Constructor for Game class.

        Parameters:
        start_flag (bool): flag to determine if game should start (default=False)
        game_mode (str): specifies single player or multiplayer mode (default=cf.SINGLE_PLAYER_MODE)

        Sets up game attributes, including start flag, default grid, current grid,
        menu grid, possible moves, and game mode.
        """
        self.default_grid = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        self.current_grid = self.default_grid
        self.menu_grid = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
        self.possible_moves = [str(num) for num in range(1, 10)]
        self.mode = None
        self.playing = None

    
    def convert_move_to_coordinate(self, moveStr):
        move_number = int(moveStr)
        move_index = move_number - 1

        if move_index < 3:
            # Row 1
            row_index = 0
        elif move_index < 6:
            # Row 2
            row_index = 1
        else:
            # Row 3
            row_index = 2
        
        col_index = move_index % 3

        return row_index, col_index
    
    def update_current_grid(self, move_coordinate, symbol):
        if symbol:
            row = move_coordinate[0]
            column = move_coordinate[1]
            self.current_grid[row][column] = symbol

    def update_possible_moves(self, moveStr):
        removeIndex = self.possible_moves.index(moveStr)
        self.possible_moves.pop(removeIndex)



    def get_columns(self):
        matrix = self.get_current_grid()
        num_rows = len(matrix)
        num_cols = num_rows
        
        columns = []
        for j in range(num_cols):
            column = []
            for i in range(num_rows):
                column.append(matrix[i][j])
            columns.append(column)
        return columns
    
    def get_diagonals(self):
        matrix = self.get_current_grid()
        num_rows = len(matrix)

        diagonal_1 = []
        diagonal_2 = []

        range_1 = list(range(num_rows))
        range_2 = list(range(num_rows - 1, -1, -1))

        for i in range(num_rows):
            item_1 = matrix[range_1[i]][range_1[i]]
            item_2 = matrix[range_1[i]][range_2[i]]

            diagonal_1.append(item_1)
            diagonal_2.append(item_2)

        return [diagonal_1, diagonal_2]

    
    def check_for_winner(self, player_1_symbol, player_2_symbol):

        matrix = self.get_current_grid()

        num_rows = len(matrix)
        num_cols = num_rows
        winning_number = 3
        # Extract columns
        columns = self.get_columns()
        # Extract diagonals
        diagonals = self.get_diagonals()
        
        # Check rows
        matrix = self.get_current_grid()
        for row in matrix:

            if row.count(player_1_symbol) == winning_number:
                self.game_over = True
                self.winner = player_1_symbol
                return
            elif row.count(player_2_symbol) == winning_number:
                self.game_over = True
                self.winner = player_2_symbol
                return
        
        for col in columns:
            if col.count(player_1_symbol) == winning_number:
                self.game_over = True
                self.winner = player_1_symbol
                return
            elif col.count(player_2_symbol) == winning_number:
                self.game_over = True
                self.winner = player_2_symbol
                return
            
        for diag in diagonals:
            if diag.count(player_1_symbol) == winning_number:
                self.game_over = True
                self.winner = player_1_symbol
                return
            elif diag.count(player_2_symbol) == winning_number:
                self.game_over = True
                self.winner = player_2_symbol
                return
            
        if len(self.get_possible_moves()) == 0:
            self.game_over = True
            self.winner = "TIE"

    def get_current_grid(self):
        return self.current_grid
    
    def get_menu_grid(self):
        return self.menu_grid

    def get_possible_moves(self):
        return self.possible_moves
    
    def get_game_over_status(self):
        return self.game_over

    def get_winner(self) -> str:
        return self.winner
    

    # Setters

    def set_mode(self, mode) -> None:
        self.mode = mode

    def set_difficulty(self, level) -> None:
        self.set_difficulty = level

    