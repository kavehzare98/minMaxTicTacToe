class Game:
    """
    Game(dim: int)

        A class to manage the core game logic of a generic square-based grid game.

    Attributes:
    ----------
        dimension : int
            An integer that determines the dimensions of the board and gets used to set total number of elements.
        default_state : list
            A list representing the initial state of the board, using '-' for empty.
        menu_state : list
            A list of strings representing the default user input choices, e.g., ['1', '2', ..., '9'].
        current_state : list
            A list representing the current state of the board.
        possible_moves : list
            A list of remaining valid move options.
        winner : str or None
            Tracks the winner's symbol ('X', 'O', etc.), or None if the game is ongoing or drawn.

    Methods:
    -------
        validate_move(move: int) -> bool
            Checks if a move is in the list of valid moves.

        update_current_state(move: int, symbol: str) -> None
            Updates the current board state with a symbol at a given move position.

        update_possible_moves(move: int) -> None
            Removes a move from the list of possible moves after it is played.

        is_draw() -> bool
            Returns True if the game is a draw (no empty cells and no winner).

        get_dimension(self) -> int
            Returns the number of columns
        
        get_rows() -> list
            Returns the board as a list of rows.

        get_cols() -> list
            Returns the board as a list of columns.

        get_diags() -> tuple
            Returns the two diagonals of the board as a tuple of lists.

        is_winner(p1_symbol, p2_symbol) -> bool
            Checks all rows, columns, and diagonals for a winning condition.

        reset_game() -> None
            Resets the board to its default state, clearing the winner and moves.
    """

    def __init__(self, dim: int = 3):
        self.dimension = dim
        num_elements = dim ** 2
        self.default_state = ['-' for i in range(num_elements)]
        self.menu_state = [str(i) for i in range(1,num_elements+1)]
        self.current_state = self.default_state.copy()
        self.possible_moves = self.menu_state.copy()
        self.winner = None

    # GETTERS
    def get_dimension(self) -> int:
        return self.dimension
    def get_default_state(self) -> list:
        return self.default_state
    
    def get_menu_state(self) -> list:
        return self.menu_state
    
    def get_current_state(self) -> list:
        return self.current_state
    
    def get_possible_moves(self) -> list:
        return self.possible_moves
    
    def get_winner(self) -> str:
        return self.winner
    
    # SETTERS
    def set_default_state(self, new_state : list) -> None:
        self.default_state = new_state

    def set_menu_state(self, new_state : list) -> None:
        self.menu_state = new_state

    def set_current_state(self, new_state : list) -> None:
        self.current_state = new_state
        
    def set_possible_moves(self, new_moves : list) -> None:
        self.possible_moves = new_moves

    # HELPER FUNCTIONS
    
    def get_rows(self) -> list:
        state = self.get_dimension()
        num_cols = int(len(state) ** 0.5)
        rows = [state[i:i+num_cols] for i in range(0, len(state), num_cols)]
        return rows
    
    def get_cols(self) -> list:
        state = self.current_state
        num_cols = self.get_dimension()
        cols = []
        for i in range(num_cols):
            col = []
            for j in range(i, len(state), num_cols):
                col.append(state[j])
            cols.append(col)
        return cols
    
    def get_diags(self) -> list:
        state = self.current_state
        num_cols = self.get_dimension()
        backward_diag = []
        forward_diag = []

        for i in range(1, num_cols + 1):
            backward_diag.append(state[(i - 1) * (num_cols + 1)])
            forward_diag.append(state[i * (num_cols - 1)])

        return (backward_diag, forward_diag)
    
    # SPECIAL METHODS
    def validate_move(self, move : int) -> bool:
        if move in self.possible_moves:
            return True
        return False
    
    def update_current_state(self, move: int, symbol: str) -> None:
        move_index = move - 1
        self.current_state[move_index] = symbol

    def update_possible_moves(self, move : int) -> None:
        move_str = str(move)
        index = self.possible_moves.index(move_str)
        self.possible_moves.pop(index)
    
    def is_draw(self) -> bool:
        if self.winner == None:
            empty_count = self.current_state.count('-')
            if empty_count == 0:
                return True
        return False

    # DETERMINE WINNER
    def is_winner(self, p1_symbol, p2_symbol) -> bool:
        winning_num = self.get_dimension()
        found_winner = False

        # Call helper functions get lists of rows, columns, and diagonals
        rows = self.get_rows()
        cols = self.get_cols()
        diags = self.get_diags()

        # Check rows for winning condition
        for row in rows:
            if found_winner == False:
                if row.count(p1_symbol) == winning_num:
                    self.winner = p1_symbol
                    found_winner = True
                elif row.count(p2_symbol) == winning_num:
                    self.winner = p2_symbol
                    found_winner = True

        # If winner found, quit function
        if found_winner:
            return found_winner
        
        # Check columns for winning condition
        for col in cols:
            if found_winner == False:
                if col.count(p1_symbol) == winning_num:
                    self.winner = p1_symbol
                    found_winner = True
                elif col.count(p2_symbol) == winning_num:
                    self.winner = p2_symbol
                    found_winner = True
        
        if found_winner:
            return found_winner

        # Check forward and backward diagonals for winning condition
        for diag in diags:
            if found_winner == False:
                if diag.count(p1_symbol) == winning_num:
                    self.winner = p1_symbol
                    found_winner = True
                elif diag.count(p2_symbol) == winning_num:
                    self.winner = p2_symbol
                    found_winner = True

        return found_winner
    
    # RESET GAME
    def reset_game(self) -> None:
        self.current_state = self.default_state.copy()
        self.possible_moves = self.menu_state.copy()
        self.winner = None