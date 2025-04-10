from view.cli_view import CommandLineInterface as CLI
from model.game import Game
import config as CONF


class GameController:
    def __init__(self, game: Game, view: CLI):
        self.game = game
        self.view = view
        self.player1 = None
        self.player2 = None
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
            
            # Ask for single or multiplayer mode (game mode)
            keep_asking = True
            while keep_asking:
                try: 
                    raw_input = self.view.prompt_user_for_game_mode()
                    game_mode_int = int(raw_input)
                except:
                    print("INPUT ERROR: Please enter a number!")
                    continue
                
                valid_game_mode = self.validate_input(game_mode_int, CONF.PLAYER_MODE_DICT.keys(), int)
                if valid_game_mode:
                    self.game.set_mode(game_mode_int)
                    keep_asking = False

            # Prompt for symbol
        
            # For single player mode
            mode = self.game.get_mode()
            if mode == CONF.PLAYER_MODE_DICT[1]:

                # Prompt user for difficulty level 
                keep_asking = True
                while keep_asking:
                    try:
                        raw_input = self.view.prompt_user_for_difficulty()
                        difficulty_level_int = int(raw_input)
                    except:
                        print("INPUT ERROR: Please enter a number!")
                        continue

                    valid_difficulty_level = self.validate_input(difficulty_level_int, CONF.DIFFICULTY_LEVEL_DICT.keys(), int)
                    if valid_difficulty_level:
                        self.game.set_difficulty(difficulty_level_int)
            else:

                    


    def run_gui(self):
        pass
    
    

        
