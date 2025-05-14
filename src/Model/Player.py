from src.Model.Config import Mode
from typing import Tuple
import random

class Player:
    """
    Represents a player in the Tic Tac Toe game. The player can be human or AI,
    with different difficulty levels for AI-controlled players.
    """

    def __init__(self):
        """
        Initializes a new Player instance.

        Args:
            difficulty_mode (int): The difficulty level of the player.
                                   Defaults to Mode.HUMAN.
        """
        self.symbol = None
        self.name = None
        self.score = 0
        self.difficulty_mode = None
        self.is_human = None

    # ========= GETTERS =========

    def get_symbol(self) -> str:
        """Returns the player's symbol ('X' or 'O')."""
        return self.symbol
    
    def get_human_flag(self) -> bool:
        """Returns whether the player is human."""
        return self.is_human
    
    def get_name(self) -> str:
        """Returns the player's name."""
        return self.name
    
    def get_difficulty_mode(self) -> int:
        """Returns the player's difficulty mode (HUMAN, EASY, MEDIUM, HARD)."""
        return self.difficulty_mode
    
    def get_score(self) -> int:
        """Returns the current score of the player."""
        return self.score

    # ========= SETTERS =========

    def set_symbol(self, new_symbol: str) -> None:
        """Sets the player's symbol (typically 'X' or 'O')."""
        self.symbol = new_symbol
    
    def set_human_flag(self, new_flag: bool) -> None:
        """Sets whether the player is human."""
        self.is_human = new_flag

    def set_name(self, new_name: str) -> None:
        """Sets the player's name."""
        self.name = new_name

    def set_difficulty_mode(self, new_mode: int) -> None:
        """Sets the difficulty level of the player."""
        self.difficulty_mode = new_mode
        if self.difficulty_mode == Mode.HUMAN:
            self.set_human_flag(True)
        else:
            self.set_human_flag(False)

    def set_score(self, new_score: int) -> None:
        """Sets the player's score."""
        self.score = new_score

    # ========= SPECIAL METHODS =========

    def move_request(self, possible_moves: list, state_dimension: int) -> int:
        """
        Determines and returns the move based on difficulty or player type.

        Args:
            possible_moves (list): A list of currently available move positions as strings.
            state_dimension (int): The dimension of the game board (e.g., 3 for 3x3).

        Returns:
            Tuple[int, str]: A tuple with the mode of the move and the selected move position.
        """
        
        if self.difficulty_mode == Mode.EASY:
            move = self.calculate_easy_move(possible_moves)
        
        elif self.difficulty_mode == Mode.MEDIUM:
            move = self.calculate_medium_move(possible_moves, state_dimension)
        
        elif self.difficulty_mode == Mode.HARD:
            move = self.calculate_hard_move(possible_moves, state_dimension)
            
        move_int = int(move)
        return move_int

    # ========= MOVE LOGIC METHODS =========

    def calculate_easy_move(self, possible_moves: list) -> str:
        """
        Selects a random move from the list of available moves.

        Args:
            possible_moves (list): Available moves.

        Returns:
            int: The chosen move as an integer.
        """
        move_choice = random.choice(possible_moves)
        return move_choice
    
    def calculate_medium_move(self, possible_moves: list, state_dimension: int) -> str:
        """
        Selects a move by preferring corners and center tiles, then defaults to random.

        Args:
            possible_moves (list): Available moves.
            state_dimension (int): The dimension of the game board.

        Returns:
            int: The chosen move.
        """
        dim = state_dimension
        corners = [0, dim - 1, dim * (dim - 1), (dim + 1) * (dim - 1)]

        if dim % 2 == 0:
            center_top_left = (corners[0] + corners[-1]) // 2
            center_bottom_left = center_top_left + dim
            center = [center_top_left, center_top_left + 1, center_bottom_left, center_bottom_left + 1]
        else:
            center = [(corners[0] + corners[-1]) // 2]

        preferred_indices = corners + center
        preferred_choices = [str(index + 1) for index in preferred_indices]
        random.shuffle(preferred_choices)

        for choice in preferred_choices:
            if choice in possible_moves:
                return choice

        # Fallback to a random move
        return random.choice(possible_moves)
    
    def calculate_hard_move(self, possible_moves: list, state_dimension: int) -> str:
        """
        Placeholder for hard mode logic (e.g., Minimax algorithm).

        Args:
            possible_moves (list): Available moves.
            state_dimension (int): Board size.

        Returns:
            int: Selected move (currently always returns 0).
        """
        return '0'

    # ========= SCORE METHOD =========

    def update_score(self, increment: int) -> int:
        """
        Updates the player's score by a given increment.

        Args:
            increment (int): The amount to increase the score by.

        Returns:
            int: The new score.
        """
        self.score += increment
        return self.score