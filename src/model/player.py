import config as cf
from random import choice
from model import game

class Player():
    def __init__(self, type: str, symbol: str, difficulty: int):
        self.type = type
        self.symbol = symbol
        self.win_status = None
        self.difficulty = difficulty

    def make_move(self, game_object: game.Game) -> str:
        if self.type == cf.COMPUTER_TYPE and self.difficulty == cf.EASY_DIFFICULTY and isinstance(game_object, game.Game):
            moves = game_object.get_possible_moves()
            computer_move = choice(moves)
            return computer_move
        else:
            user_input = input("Enter your move:\t")
            return user_input
    
    # Getters
    def get_player_type(self) -> str:
        return self.type
    
    def get_player_symbol(self) -> str:
        return self.symbol
    
    def get_win_status(self)-> bool:
        return self.win_status
    
    def get_difficulty(self) -> int:
        return self.difficulty
    
    # Setters
    def set_player_type(self, new_type: str):
        self.type = new_type
    
    def set_player_symbol(self, new_symbol: str):
        self.symbol = new_symbol

    def set_win_status(self, new_win_status: bool):
        self.win_status = new_win_status

    def set_difficulty(self, new_difficulty: int):
        self.difficulty = new_difficulty