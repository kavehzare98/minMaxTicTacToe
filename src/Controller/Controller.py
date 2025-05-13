from ..View.CommandLineView import CommandLineView
from ..Model.Game import Game
from ..Model.Player import Player
from ..Model.Config import Mode

class Controller:
    def __init__(self):
        self.player_1   = Player()
        # Setter for Player class will set the is_human flag accordingly when called
        self.player_1.set_difficulty_mode(Mode.HUMAN)   # First player is always a HUMAN
        self.player_1.set_symbol('X')

        self.player_2   = Player()
        self.player_2.set_symbol('O')

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

        # Game constants, defined in one place
        menu_state =        self.game.get_menu_state()
        dimension =         self.game.get_dimension()

        # ====== START ====== PROMPT & INPUT VALIDATION
        # Prompt the user if they want to play
        raw_start_response = self.view.prompt_to_start()
        clean_start_response = self.clean_user_input(raw_start_response)

        # Extract the first character of the cleaned (stripped and lowercase) response
        char_start_response = self.extract_first_char(clean_start_response)

        # Validate the response
        valid_responses = self.get_possible_yes_no()
        is_valid_start = self.validate_input(char_start_response, valid_responses)
        # ====== END ====== PROMPT & INPUT VALIDATION

        # Get Player Symbols
        player_1_symbol = self.player_1.get_symbol()
        player_2_symbol = self.player_2.get_symbol()

        while is_valid_start and char_start_response == 'y':

            # ASK PLAYER FOR NAME, CLEAN, and SET as Player 1 Name
            raw_name_input = self.view.prompt_for_name()
            clean_name_input = self.clean_user_input(raw_name_input)
            self.player_1.set_name(clean_name_input)

            # ASK PLAYER FOR MODE
            raw_mode = self.view.prompt_for_mode()
            clean_mode = self.clean_user_input(raw_mode)

            valid_modes = self.get_possible_modes()
            is_valid_mode = self.validate_input(clean_mode, valid_modes)

            
            if is_valid_mode:
                
                # Convert the Mode to Integer format
                mode_int = int(clean_mode)

                # Set the Mode for Player 2
                self.player_2.set_difficulty_mode(mode_int)

                current_winner = self.game.get_winner()
                
                if mode_int == Mode.HUMAN:
                    # ASK PLAYER FOR NAME, CLEAN, and SET as Player 2 Name
                    raw_name_input = self.view.prompt_for_name()
                    clean_name_input = self.clean_user_input(raw_name_input)
                    self.player_2.set_name(clean_name_input)
                else:
                    self.player_2.set_name("Computer")

                # Game Loop
                while current_winner == None:

                    # Get Current State, and Possible Moves
                    current_state =     self.game.get_current_state()
                    possible_moves =    self.game.get_possible_moves()

                    # Obtain Player 1 Mode and Move
                    p1_mode, p1_move =  self.player_1.move_request(possible_moves, dimension)

                    # Take & Validate p1 move
                    self.view.display_grid(menu_state, "MENU")
                    self.view.display_error(current_state, "CURRENT")
                    raw_p1_move_input = self.view.prompt_for_move(self.player_1.get_name())
                    clean_p1_move_input = self.clean_user_input(raw_p1_move_input)
                    is_valid_p1_move = self.validate_input(clean_p1_move_input, possible_moves)


                    # Multiplayer Scenario
                    if is_valid_p1_move and self.player_2.get_human_flag():
                        
                        # Update Current State and Possible Moves
                        p1_move_int = int(clean_p1_move_input)
                        self.game.update_current_state(p1_move_int, player_1_symbol)
                        self.game.update_possible_moves(p1_move_int)
                        
                        updated_current_state = self.game.get_current_state()
                        updated_possible_moves = self.game.get_possible_moves()

                        # Take & Validate p2 move
                        self.view.display_grid(menu_state, "MENU")
                        self.view.display_error(current_state, "CURRENT")
                        raw_p2_move_input = self.view.prompt_for_move(self.player_2.get_name())
                        clean_p2_move_input = self.clean_user_input(raw_p2_move_input)
                        is_valid_p2_move = self.validate_input(clean_p2_move_input, possible_moves)




                    # Single Player
                    elif is_valid_p1_move:
                        # Update Current State and Possible Moves
                        p1_move_int = int(clean_p1_move_input)
                        self.game.update_current_state(p1_move_int, player_1_symbol)
                        self.game.update_possible_moves(p1_move_int)
                        
                        updated_current_state = self.game.get_current_state()
                        updated_possible_moves = self.game.get_possible_moves()

            

                   
                    # Check for Winner
                    is_draw = self.game.check_for_draw()
                    is_winner = self.game.check_for_winner()
                        
                    if is_draw == False and is_winner == False:
                        p2_mode, p2_move =  self.player_2.move_request(updated_possible_moves, dimension)

                    elif is_draw == True:
                        self.view.display_tie()
                    


                # SHOWS GAME OVER
                self.view.display_footer()
            
            # AFTER GAME OVER, REPROMPT
            # ====== START ====== PROMPT & INPUT VALIDATION
            # Prompt the user if they want to play
            raw_start_response = self.view.prompt_to_start()
            clean_start_response = self.clean_user_input(raw_start_response)

            # Extract the first character of the cleaned (stripped and lowercase) response
            char_start_response = self.extract_first_char(clean_start_response)

            # Validate the response
            valid_responses = self.get_possible_yes_no()
            is_valid_start = self.validate_input(char_start_response, valid_responses)
            # ====== END ====== PROMPT & INPUT VALIDATION

        # QUIT GAME #! FIX LATER, This shouldn't be handled by Controller
        print("\nGOOD BYE...\n")