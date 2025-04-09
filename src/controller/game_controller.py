from view.cli_view import CommandLineInterface as CLI
from model.game import Game
import config as CONF


class GameController:
    def __init__(self, game: Game, player, view: CLI):
        self.game = game
        self.player = player
        self.view = view
        self.running = False

    # Parse input
    def get_first_char(self, raw_input: str) -> str:
        lower_input = raw_input.lower()
        first_char = lower_input[0]
        return first_char
    

    
    def get_valid_start_response(self, valid_responses):
        # Input validation for start of game
        keep_asking = True
        while keep_asking:

            raw_input = self.view.prompt_user_to_start_game()
            start_first_char = self.get_first_char(raw_input)

            if start_first_char not in valid_responses:
                print("INVALID INPUT: Please try again.")
                continue
            else:
                keep_asking = False

    def validate_input(self, user_input, valid_range, expected_type=str) -> bool:
        valid = False
        if isinstance(user_input, expected_type) and (user_input in valid_range):
            valid = True
        return valid
        
    def run_cli(self):
        
        keep_asking = True
        while keep_asking:
            raw_input = self.view.prompt_user_to_start_game()
            start_first_char = self.get_first_char(raw_input)
            valid_response = self.validate_input(start_first_char, CONF.START_CHOICES)
            if valid_response:
                keep_asking = False

        # Check if user wants to start game
        if start_first_char == 'y':
            self.running = True

        while (self.running):
            game_mode = self.view.prompt_user_for_game_mode()
            keep_asking = True
            while keep_asking:
                try: 
                    raw_input = self.view.prompt_user_for_game_mode()
                    game_mode_int = int(raw_input)
                except:
                    print("INPUT ERROR: Please enter a number!")
                    continue
                
                valid_game_mode = self.validate_input(game_mode_int, CONF.DIFFICULTY_LEVEL_DICT.keys(), int)
                if valid_game_mode:
                    


    def run_gui(self):
        pass
    
    

        
