import config as cf
from game import Game
from player import Player


def main():

    oGame = Game()
    oGame.displayHeader()
    oGame.askToStartGame()

    while oGame.getStartFlag():
        gridChoice = oGame.getGrid("menu")
        oGame.displayGrid(gridChoice)
        
        gridChoice = oGame.getGrid("current")
        oGame.displayGrid(gridChoice)
        oGame.askToStartGame()

    oGame.displayFooter()




main()