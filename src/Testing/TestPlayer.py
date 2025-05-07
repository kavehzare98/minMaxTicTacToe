from Model.Player import Player
import unittest


# TEST LATER
# class TestPlayer(unittest.TestCase):
#     

'''

# ========= SPECIAL METHODS =========

def move_request(self, possible_moves: list, state_dimension: int) -> Tuple[int, str]:
    """
    Determines and returns the move based on difficulty or player type.

    Args:
        possible_moves (list): A list of currently available move positions as strings.
        state_dimension (int): The dimension of the game board (e.g., 3 for 3x3).

    Returns:
        Tuple[int, int]: A tuple with the mode of the move and the selected move position.
    """
    if self.is_human:
        return (Mode.HUMAN, '0')
    
    elif self.difficulty_mode == Mode.EASY:
        move = self.calculate_easy_move(possible_moves)
        return (Mode.EASY, move)
    
    elif self.difficulty_mode == Mode.MEDIUM:
        move = self.calculate_medium_move(possible_moves, state_dimension)
        return (Mode.MEDIUM, move)
    
    elif self.difficulty_mode == Mode.HARD:
        move = self.calculate_hard_move(possible_moves, state_dimension)
        return (Mode.HARD, move)

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

'''

