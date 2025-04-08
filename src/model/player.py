import config as cf
from random import choice
from model import game

class Player():
    def __init__(self, type=cf.COMPUTER_TYPE, symbol=cf.COMPUTER_SYMBOL, difficulty=cf.EASY_DIFFICULTY):
        self.type = type
        self.symbol = symbol
        self.winStatus = None
        self.difficulty = difficulty

    def makeMove(self, gameObject):
        if self.type == cf.COMPUTER_TYPE and self.difficulty == cf.EASY_DIFFICULTY and isinstance(gameObject, game.Game):
            moves = gameObject.get_possible_moves()
            computer_move = choice(moves)
            return computer_move
        else:
            user_input = input("Enter your move:\t")
            return user_input

    
    def getPlayerType(self):
        return self.type
    
    def getPlayerSymbol(self):
        return self.symbol
    
    def getWinStatus(self):
        return self.winStatus
    
    def setPlayerType(self, newType):
        self.type = newType
    
    def setPlayerSymbol(self, newSymbol):
        self.symbol = newSymbol

    def setWinStatus(self, newWinStatus):
        self.winStatus = newWinStatus

    # make move

