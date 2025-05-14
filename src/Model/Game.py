class Game:
    """
    Game(dim: int = 3)

    Core game logic handler for a square grid game such as Tic Tac Toe.
    Maintains game state, validates moves, determines win/draw conditions,
    and supports game resets.

    Attributes:
    -----------
    dimension : int
        Dimension of the square grid (e.g., 3 for a 3x3 board).
    default_state : list
        The initial empty board state using '-' to represent unoccupied tiles.
    menu_state : list
        User-facing labels for each tile (e.g., ['1', ..., '9']).
    current_state : list
        The current state of the game board.
    possible_moves : list
        The list of valid move labels that haven't been played yet.
    winner : str or None
        Tracks the winning symbol (e.g., 'X', 'O') or None if no winner.
    """

    def __init__(self, dim: int = 3):
        """
        Initializes a new game with a square board of dimension dim x dim.
        """
        self.dimension = dim
        num_elements = dim ** 2
        self.default_state = ['-' for _ in range(num_elements)]
        self.menu_state = [str(i) for i in range(1, num_elements + 1)]
        self.current_state = self.default_state.copy()
        self.possible_moves = self.menu_state.copy()
        self.winner = None

    # ======== GETTERS ========

    def get_dimension(self) -> int:
        """Returns the dimension of the game board."""
        return self.dimension

    def get_default_state(self) -> list:
        """Returns the initial empty state of the game board."""
        return self.default_state

    def get_menu_state(self) -> list:
        """Returns the display labels for the game board (e.g., ['1', ..., '9'])."""
        return self.menu_state

    def get_current_state(self) -> list:
        """Returns the current board state."""
        return self.current_state

    def get_possible_moves(self) -> list:
        """Returns the remaining possible moves."""
        return self.possible_moves

    def get_winner(self) -> str:
        """Returns the symbol of the winner, or None if no winner exists yet."""
        return self.winner

    # ======== SETTERS ========

    def set_default_state(self, new_state: list) -> None:
        """Sets a new default state for the game."""
        self.default_state = new_state

    def set_menu_state(self, new_state: list) -> None:
        """Sets a new menu state for user-facing tile labels."""
        self.menu_state = new_state

    def set_current_state(self, new_state: list) -> None:
        """Sets the current state of the board."""
        self.current_state = new_state

    def set_possible_moves(self, new_moves: list) -> None:
        """Sets the list of valid moves."""
        self.possible_moves = new_moves

    def set_winner(self, winner: str) -> None:
        """Sets the winner of the game."""
        self.winner = winner

    # ======== BOARD STRUCTURE HELPERS ========

    def get_rows(self) -> list:
        """
        Returns the current board state divided into rows.
        """
        state = self.current_state
        dim = self.get_dimension()
        return [state[i:i + dim] for i in range(0, len(state), dim)]

    def get_cols(self) -> list:
        """
        Returns the current board state divided into columns.
        """
        state = self.current_state
        dim = self.get_dimension()
        return [[state[i + j * dim] for j in range(dim)] for i in range(dim)]

    def get_diags(self) -> tuple:
        """
        Returns both diagonals from the board.

        Returns:
            tuple: (backward_diag, forward_diag)
                - backward_diag: top-left to bottom-right
                - forward_diag: top-right to bottom-left
        """
        state = self.current_state
        dim = self.get_dimension()

        backward_diag = [state[i * (dim + 1)] for i in range(dim)]
        forward_diag = [state[(i + 1) * (dim - 1)] for i in range(dim)]

        return (backward_diag, forward_diag)

    # ======== GAMEPLAY METHODS ========

    #! Useless
    def validate_move(self, move: str) -> bool:
        """
        Checks if the move is valid (still available).

        Args:
            move (int): The move position entered by the player.

        Returns:
            bool: True if move is valid, False otherwise.
        """
        return move in self.possible_moves

    def update_current_state(self, move: int, symbol: str) -> None:
        """
        Applies a move to the board state.

        Args:
            move (int): Board position to update.
            symbol (str): Player's symbol ('X' or 'O').
        """
        self.current_state[move - 1] = symbol

    def update_possible_moves(self, move: int) -> None:
        """
        Removes a move from the list of valid options.

        Args:
            move (int): The move to remove.
        """
        self.possible_moves.remove(str(move))

    def check_for_draw(self) -> bool:
        """
        Determines if the game has ended in a draw (no more moves and no winner).

        Returns:
            bool: True if draw, False otherwise.
        """
        return self.winner is None and '-' not in self.current_state

    def check_for_winner(self, p1_symbol: str, p2_symbol: str) -> bool:
        """
        Checks the board for a winning condition for either player.

        Args:
            p1_symbol (str): First player's symbol.
            p2_symbol (str): Second player's symbol.

        Returns:
            bool: True if either player has won.
        """
        dim = self.get_dimension()
        rows = self.get_rows()
        cols = self.get_cols()
        diags = self.get_diags()

        # Check all rows, columns, and diagonals for a win
        for group in rows + cols + list(diags):
            if group.count(p1_symbol) == dim:
                self.winner = p1_symbol
                return True
            elif group.count(p2_symbol) == dim:
                self.winner = p2_symbol
                return True

        return False

    def reset_game(self) -> None:
        """
        Resets the game state to its original values.
        Clears the board, restores possible moves, and removes the winner.
        """
        self.current_state = self.default_state.copy()
        self.possible_moves = self.menu_state.copy()
        self.winner = None
