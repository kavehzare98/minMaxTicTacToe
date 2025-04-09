import config as cf
from random import choice
from model import game

class Player():
    def __init__(self, type=cf.COMPUTER_TYPE, symbol=cf.COMPUTER_SYMBOL, difficulty=cf.EASY_DIFFICULTY):
        self.type = type
        self.symbol = symbol
        self.win_status = None
        self.difficulty = difficulty

    def make_move(self, game_object):
        if self.type == cf.COMPUTER_TYPE and self.difficulty == cf.EASY_DIFFICULTY and isinstance(game_object, game.Game):
            moves = game_object.get_possible_moves()
            computer_move = choice(moves)
            return computer_move
        else:
            user_input = input("Enter your move:\t")
            return user_input

    
    def get_player_type(self):
        return self.type
    
    def get_player_symbol(self):
        return self.symbol
    
    def get_win_status(self):
        return self.win_status
    
    def set_player_type(self, new_type):
        self.type = new_type
    
    def set_player_symbol(self, new_symbol):
        self.symbol = new_symbol

    def set_win_status(self, new_win_status):
        self.win_status = new_win_status

    # make move

