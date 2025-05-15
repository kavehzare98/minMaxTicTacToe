from ..View.CommandLineView import CommandLineView
from ..Model.Game import Game
from ..Model.Player import Player
from ..Model.Config import Mode
import random

class Controller:
    def __init__(self):
        self.player_1   = Player()
        self.player_2   = Player()
        self.game       = Game(dim=3)
        self.view       = CommandLineView()
        self.possible_yes_no = ['y', 'n', 'q']
        self.possible_modes = [str(num) for num in range(4)]
        self.keep_playing = True
        self.possible_symbols = ['X', 'O']

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
    
    def get_possible_modes(self) -> list:
        return self.possible_modes
    
    def get_keep_playing(self) -> bool:
        return self.keep_playing

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

    def set_possible_modes(self, modes: list) -> None:
        self.possible_modes = modes

    def set_keep_playing(self, new_flag: bool) -> None:
        self.keep_playing = new_flag

    # ==== SPECIAL METHODS ====
    def clean_user_input(self, input: str) -> str:
        """
        This function strips white space around the input.
        """
        return input.strip()
    
    def extract_first_char(self, input: str) -> str:
        first_char = input[0]
        return first_char

    def validate_input(self, input: str, valid_inputs: list) -> bool:
        valid_flag = False 
        if input in valid_inputs:
            valid_flag = True
        return valid_flag
    
    def run(self):
        # Display Welcome to Tic Tac Toe (View)
        self.view.display_welcome()

        # Prompt for Start (View), Clean, Extract First Char
        raw_start_input     = self.view.prompt_for_start()
        clean_start_input   = self.clean_user_input(raw_start_input)
        char_start_input    = self.extract_first_char(clean_start_input)
        
        # First check to start game, if not 'y', then 
        if char_start_input in ['y', 'Y']:

            # Always set Player 1 mode to HUMAN
            self.player_1.set_difficulty_mode(Mode.HUMAN)
            
            # Prompt for Name, Clean, Set Player's name
            raw_player_1_name_input     = self.view.prompt_for_name()
            clean_player_1_name_input   = self.clean_user_input(raw_player_1_name_input)
            self.player_1.set_name(clean_player_1_name_input)

            # Prompt for Symbol, Clean, Extract First Char, Set Player 1 Symbol
            raw_player_1_symbol_input   = self.view.prompt_for_symbol()
            clean_player_1_symbol_input = self.clean_user_input(raw_player_1_symbol_input)
            char_player_1_symbol_input  = self.extract_first_char(clean_player_1_symbol_input)
            self.player_1.set_symbol(char_player_1_symbol_input)

            # Prompt for Mode, Clean, Extract first Char
            raw_mode_input     = self.view.prompt_for_mode()
            clean_mode_input  = self.clean_user_input(raw_mode_input)
            char_mode_input    = self.extract_first_char(clean_mode_input)

            # Validation
            while char_mode_input not in self.get_possible_modes():
                # Display ERROR MESSAGE
                self.view.display_error()
                # Prompt for Mode, Clean, Extract, Convert, Set Player 2 Mode
                raw_mode_input     = self.view.prompt_for_mode()
                clean_mode_input   = self.clean_user_input(raw_mode_input)
                char_mode_input    = self.extract_first_char(clean_mode_input)

            # Convert Difficulty Mode from String to Integer
            difficulty_mode = int(char_mode_input)

            # Set Player 2 Mode
            self.player_2.set_difficulty_mode(difficulty_mode)

            # Check Mode to Prompt for Name and Symbol Accordingly
            if difficulty_mode == Mode.HUMAN:

                # Prompt for Name, Clean, Set Player 2 name
                raw_player_2_name_input     = self.view.prompt_for_name()
                clean_player_2_name_input   = self.clean_user_input(raw_player_2_name_input)
                self.player_2.set_name(clean_player_2_name_input)

                # Prompt for Symbol, Clean, Extract First Char, Set Player 2 Symbol
                raw_player_2_symbol_input   = self.view.prompt_for_symbol()
                clean_player_2_symbol_input = self.clean_user_input(raw_player_2_symbol_input)
                char_player_2_symbol_input  = self.extract_first_char(clean_player_2_symbol_input)
                self.player_2.set_symbol(char_player_2_symbol_input)

            else:
                
                # Set Player 2 (computer) name
                player_name = "Computer"
                self.player_2.set_name(player_name)
                
                # Set Player 2 Symbol
                if self.player_1.get_symbol() in self.possible_symbols:
                    self.possible_symbols.remove(self.player_1.get_symbol())
                rand_symbol = random.choice(self.possible_symbols)
                self.player_2.set_symbol(rand_symbol)

            # Game Loop Starts here
            while self.keep_playing == True and char_start_input in ['y', 'Y']:
                
                # Display Menu and Current State
                self.view.display_grid(self.game.get_menu_state(), "MENU")
                self.view.display_grid(self.game.get_current_state(), "CURRENT")

                # Prompt Player 1 for Move, validate move
                raw_player_1_move_input = self.view.prompt_for_move(self.player_1.get_name())
                clean_player_1_move_input = self.clean_user_input(raw_player_1_move_input)
                
                # Validate Move
                is_valid_move = self.game.validate_move(clean_player_1_move_input)
                while is_valid_move == False:
                    # Display Error message
                    self.view.display_error()
                    # Prompt Player 1 for Move, validate move
                    raw_player_1_move_input = self.view.prompt_for_move(self.player_1.get_name())
                    clean_player_1_move_input = self.clean_user_input(raw_player_1_move_input)
                    is_valid_move = self.game.validate_move(clean_player_1_move_input)

                # Convert Move to Integer, Update Current State and Possible Moves
                player_1_move_int = int(clean_player_1_move_input)
                self.game.update_current_state(player_1_move_int, self.player_1.get_symbol())
                self.game.update_possible_moves(player_1_move_int)
                
                # Check for draw and winner (Game)
                is_draw     = self.game.check_for_draw()
                is_winner   = self.game.check_for_winner(self.player_1.get_symbol(), self.player_2.get_symbol())
                
                # Check if it's a tie or a winning situation
                if is_draw == False and is_winner == False:
                    
                    # Multiplayer mode
                    if self.player_2.get_difficulty_mode() == Mode.HUMAN:
                        # Display Menu and Current State
                        self.view.display_grid(self.game.get_menu_state(), "MENU")
                        self.view.display_grid(self.game.get_current_state(), "CURRENT")

                        # Prompt Player 1 for Move, validate move
                        raw_player_2_move_input = self.view.prompt_for_move(self.player_2.get_name())
                        clean_player_2_move_input = self.clean_user_input(raw_player_2_move_input)
                        
                        # Validate Move
                        is_valid_move = self.game.validate_move(clean_player_2_move_input)
                        while is_valid_move == False:
                            # Display Error message
                            self.view.display_error()
                            # Prompt Player 2 for Move, validate move
                            raw_player_2_move_input = self.view.prompt_for_move(self.player_2.get_name())
                            clean_player_2_move_input = self.clean_user_input(raw_player_2_move_input)
                            is_valid_move = self.game.validate_move(clean_player_2_move_input)
                       
                        # Convert string move to integer
                        player_2_move_int = int(clean_player_2_move_input)
                    
                    # Single Player mode
                    else:
                        player_2_move_int = self.player_2.move_request(self.game.get_possible_moves(), self.game.get_dimension())

                    # Update Current State and Possible Moves
                    self.game.update_current_state(player_2_move_int, self.player_2.get_symbol())
                    self.game.update_possible_moves(player_2_move_int)

                    # Check for draw and winner (Game)
                    is_draw     = self.game.check_for_draw()
                    is_winner   = self.game.check_for_winner(self.player_1.get_symbol(), self.player_2.get_symbol())

                    # If there are no winners or ties, skip
                    if is_draw == False and is_winner == False:
                        continue
                
                # If there is a winner or a tie
                if is_winner:
                    current_winner = self.game.get_winner()
                    if self.player_1.get_symbol() == current_winner:
                        winner_name = self.player_1.get_name()
                        self.player_1.update_score(1)
                    else:
                        winner_name = self.player_2.get_name()
                        self.player_2.update_score(1)

                        self.view.display_winner(winner_name)

                elif is_draw:
                    self.view.display_tie()

                # Display Game Over
                self.view.display_grid(self.game.get_current_state(), "FINAL")
                self.view.display_footer()

                # Display Scores
                p1_name, p2_name = self.player_1.get_name(), self.player_2.get_name()
                p1_score, p2_score = self.player_1.get_score(), self.player_2.get_score()
                self.view.display_scores(p1_name, p1_score, p2_name, p2_score)

                # Prompt for Start (View), Clean, Extract First Char
                raw_start_input     = self.view.prompt_for_start()
                clean_start_input   = self.clean_user_input(raw_start_input)
                char_start_input    = self.extract_first_char(clean_start_input)

                # Reset Game to Original State
                self.game.reset_game()

                    


                











