from ..View.CommandLineView import CommandLineView
from ..Model.Game import Game
from ..Model.Player import Player
from ..Model.Config import Mode

class Controller:
    def __init__(self):
        self.player_1   = Player()
        self.player_1.set_difficulty_mode(Mode.HUMAN)   # First player is always a HUMAN

        self.player_2   = Player()
        self.game       = Game(dim=3)
        self.view       = CommandLineView()
        self.possible_yes_no = ['y', 'n', 'q']
        self.current_player = None
        self.possible_modes = [str(num) for num in range(4)]

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
    
    def get_possible_modes(self) -> list:
        return self.possible_modes

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

    def set_possible_modes(self, modes: list) -> None:
        self.possible_modes = modes

    # ==== SPECIAL METHODS ====
    def clean_user_input(self, input: str) -> str:
        """
        This function strips white space around the input, and converts it to lower case.
        """
        cleaned_input = input.strip()
        lower_cleaned_input = cleaned_input.lower()
        return lower_cleaned_input
    
    def extract_first_char(self, input: str) -> str:
        first_char = input[0]
        return first_char

    def validate_input(self, input: str, valid_inputs: list) -> bool:
        valid_flag = False 
        if input in valid_inputs:
            valid_flag = True
        return valid_flag
    
    def run(self):
        # Display Header
        self.view.display_header()

        # ====== START ====== PROMPT & INPUT VALIDATION
        # Prompt the user if they want to play
        raw_start_response = self.view.prompt_to_start()
        clean_start_response = self.clean_user_input(raw_start_response)

        # Extract the first character of the cleaned (stripped and lowercase) response
        first_char_response = self.extract_first_char(clean_start_response)

        # Validate the response
        valid_responses = self.get_possible_yes_no()
        start_is_valid = self.validate_input(first_char_response, valid_responses)
        # ====== END ====== PROMPT & INPUT VALIDATION

        while start_is_valid and first_char_response == 'y':

            # ASK PLAYER FOR NAME, CLEAN, and SET as Player 1 Name
            raw_name_input = self.view.prompt_for_name()
            clean_name_input = self.clean_user_input(raw_name_input)
            self.player_1.set_name(clean_name_input)
            self.player_1.set_symbol('X')

            # ASK PLAYER FOR MODE
            raw_mode = self.view.prompt_for_mode()
            clean_mode = self.clean_user_input(raw_mode)

            valid_modes = self.get_possible_modes()
            mode_is_valid = self.validate_input(clean_mode, valid_modes)

            if mode_is_valid:
            
                # SHOWS GAME OVER
                self.view.display_footer()
            
            # AFTER GAME OVER, REPROMPT
            # ====== START ====== PROMPT & INPUT VALIDATION
            # Prompt the user if they want to play
            raw_start_response = self.view.prompt_to_start()
            clean_start_response = self.clean_user_input(raw_start_response)

            # Extract the first character of the cleaned (stripped and lowercase) response
            first_char_response = self.extract_first_char(clean_start_response)

            # Validate the response
            valid_responses = self.get_possible_yes_no()
            start_is_valid = self.validate_input(first_char_response, valid_responses)
            # ====== END ====== PROMPT & INPUT VALIDATION

        # QUIT GAME #! FIX LATER, This shouldn't be handled by Controller
        print("\nGOOD BYE...\n")