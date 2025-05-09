from ..View.CommandLineView import CommandLineView
from ..Model.Game import Game
from ..Model.Player import Player

class Controller:
    def __init__(self):
        self.player_1   = Player()
        self.player_2   = Player()
        self.game       = Game(dim=3)
        self.view       = CommandLineView()
        self.possible_yes_no = ['Yes', 'yes', 'YES', 'Y', 'y', 'No', 'no', 'NO', 'N', 'n']
        self.current_player = None

    # ==== GETTERS ====
    def get_player_1(self) -> Player:
        return self.player_1
    
    def get_player_2(self) -> Player:
        return self.player_2
    
    def get_game(self) -> Game:
        return self.game
    
    def get_view(self) -> CommandLineView:
        return self.view

    def get_possible_yes_no(self) -> list:
        return self.possible_yes_no
    
    def get_current_player(self) -> Player:
        return self.current_player

    # ==== SETTERS ====
    def set_player_1(self, new_player: Player) -> None:
        self.player_1 = new_player
    
    def set_player_2(self, new_player: Player) -> None:
        self.player_2 = new_player
    
    def set_game(self, new_game: Game) -> None:
        self.game = new_game
    
    def set_view(self, new_view: CommandLineView) -> None:
        self.view = new_view

    def set_possible_yes_no(self, new_list: list) -> None:
        self.possible_yes_no = new_list
    
    def set_current_player(self, new_player: Player) -> None:
        self.current_player = new_player

    # ==== SPECIAL METHODS ====
    def validate_input(self, input: str, valid_inputs: list) -> bool:
        valid_flag = False 
        if input in valid_inputs:
            valid_flag = True
        return valid_flag
    
    def run(self):
        return
    
