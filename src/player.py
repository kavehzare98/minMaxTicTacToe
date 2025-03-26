import config as cf
import game

class Player():
    def __init__(self, type=cf.COMPUTER_TYPE, symbol=cf.COMPUTER_SYMBOL):
        self.type = type
        self.symbol = symbol
        self.winStatus = None

    # def makeMove(self):
    #     if self.type == cf.COMPUTER_TYPE:
    #     else:
    
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

