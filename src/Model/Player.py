
from src.Model.Config import Mode
from typing import Tuple
import random

class Player:
    def __init__(self, difficulty_mode=Mode.HUMAN):
        self.symbol = None
        self.is_human = None
        self.name = None
        self.difficulty_mode = difficulty_mode
        self.score = 0

    # GETTERS
    def get_symbol(self) -> str:
        return self.symbol
    
    def get_human_flag(self) -> bool:
        return self.is_human
    
    def get_name(self) -> str:
        return self.name
    
    def get_difficulty_mode(self) -> int:
        return self.difficulty_mode
    
    def get_score(self) -> int:
        return self.score



    # SETTERS
    def set_symbol(self, new_symbol: str) -> None:
        self.symbol = new_symbol
    
    def set_human_flag(self, new_flag: bool) -> None:
        self.is_human = new_flag

    def set_name(self, new_name: str) -> None:
        self.name = new_name

    def set_difficulty_mode(self, new_mode: int) -> None:
        self.difficulty_mode = new_mode

    def set_score(self, new_score: int) -> None:
        self.score = new_score



    # SPECIAL METHODS
    def move_request(self, possible_moves: list, state_dimension: int) -> Tuple[int, int]:
        if self.is_human:
            return (Mode.HUMAN, 0)
        
        elif self.difficulty_mode == Mode.EASY:
            move = self.calculate_easy_move(possible_moves)
            return (Mode.EASY, move)
        
        elif self.difficulty_mode == Mode.MEDIUM:
            move = self.calculate_medium_move(possible_moves, state_dimension)
            return (Mode.MEDIUM, move)
        
        elif self.difficulty_mode == Mode.HARD:
            move = self.calculate_hard_move(possible_moves, state_dimension)
            return (Mode.HARD, move)
        
    # MOVE Calculations (3 Modes: Easy, Medium, Hard)
    def calculate_easy_move(self, possible_moves: list) -> int:
        # Based on completely random pick
        choice_str = random.Choice(possible_moves)
        choice_int = int(choice_str)
        return choice_int
    
    def calculate_medium_move(self, possible_moves: list, state_dimension: int) -> int:
        
        dim = state_dimension
        corners = [0, int(dim - 1), int(dim * (dim - 1)), int((dim + 1) * (dim - 1))]
        
        if dim % 2 == 0:
            center_top_left = (corners[0] + corners[-1]) // 2
            center_bottom_left = center_top_left + dim
            center = [center_top_left, center_top_left + 1, center_bottom_left, center_bottom_left + 1]
        
        else:
            center = [(corners[0] + corners[-1]) // 2]

        corners_plus_center = corners + center
        choices = [str(index + 1) for index in corners_plus_center]
        random.shuffle(choices)
        
        for choice in choices:
            if choice in possible_moves:
                move = int(choice)
                return move
                
        choice_str = random.choice(possible_moves)
        move = int(choice_str)
        return move    
    
    def calculate_hard_move(self, possible_moves: list, state_dimension: int) -> int:
        return 0

    # SCORE METHOD
    def update_score(self, increment: int) -> int:
        self.score += increment
        return self.score