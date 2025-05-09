
from .Art import Art

class CommandLineView:
    def __init__(self):
        self.start_message  =  "Would You Like to Start the Game?\t"
        self.name_message   =  "What's Your Name?\t"
        self.move_message   =  "What's Your Next Move:\t"
        self.error_message  =  "ERROR: Invalid Input!"
        self.winning_message =  "The Following Player Wins:\t"
        self.draw_message   =  "It's a TIE!"
        self.ascii_art      =  Art()
        self.mode_message   =  "Please Choose a Mode:\t"
        self.mode_menu      = """
0.\tMULTIPLAYER
1.\tEASY
2.\tMEDIUM
3.\tHARD
"""
        
    # ====== GETTERS ===========
    def get_start_message(self) -> str:
        return self.start_message
    
    def get_name_message(self) -> str:
        return self.name_message
    
    def get_move_message(self) -> str:
        return self.move_message
    
    def get_error_message(self) -> str:
        return self.error_message
    
    def get_winning_message(self) -> str:
        return self.winning_message
    
    def get_draw_message(self) -> str:
        return self.draw_message
    
    def get_mode_menu(self) -> str:
        return self.mode_menu
    
    def get_mode_message(self) -> str:
        return self.mode_message

    # ====== SETTERS ===========
    def set_start_message(self, new_message: str) -> None:
        self.start_message = new_message
    
    def set_name_message(self, new_message: str) -> None:
        self.name_message = new_message
    
    def set_move_message(self, new_message: str) -> None:
        self.move_message = new_message
    
    def set_error_message(self, new_message: str) -> None:
        self.error_message = new_message
    
    def set_winning_message(self, new_message: str) -> None:
        self.winning_message = new_message
    
    def set_draw_message(self, new_message: str) -> None:
        self.draw_message = new_message
    
    def set_mode_menu(self, new_menu: str) -> None:
        self.mode_menu = new_menu

    def set_mode_message(self, new_mode: str) -> None:
        self.mode_message = new_mode

    # ====== DISPLAYS ===========
    def display_header(self) -> None:
        print(self.ascii_art.get_welcome())
    
    def display_footer(self) -> None:
        print(self.ascii_art.get_game_over())

    def display_grid(self, state : list, state_name : str) -> None:
        print(f"{state_name}:", end='\n\n')
        dimension = int(len(state) ** 0.5)
        num_for_divider = 5 * dimension - 2
        index = 0
        for row in range(dimension):
            for col in range(dimension):
                if col < (dimension - 1):
                    print(f' {state[index]} ', end='')
                    print('||', end='')
                else:
                    print(f' {state[index]} ', end='')
                index += 1
            print()
            if row < (dimension - 1):
                print(num_for_divider * "=")
        print()

    def display_scores(self, p1_name: str, p1_score: int, p2_name : str, p2_score : int) -> None:
        print(f'\n{p1_name} Score:\t{p1_score}')
        print(f'{p2_name} Score:\t{p2_score}')

    def display_winner(self, winner_name: str) -> None:
        print(f"{self.get_winning_message()}{winner_name}")

    def display_tie(self) -> None:
        print(f'\n{self.get_draw_message()}\n')

    def display_error(self) -> None:
        print(f'\n{self.get_error_message()}\n')

    # ====== PROMPTS ===========
    def prompt_to_start(self) -> str:
        user_input = input(self.get_start_message())
        return user_input
    
    def prompt_for_name(self) -> str:
        user_input = input(self.get_name_message())
        return user_input
    
    def prompt_for_mode(self) -> str:
        print(self.get_mode_menu())
        user_input = input(self.get_mode_message())
        return user_input
    
    def prompt_for_move(self, player_name: str) -> str:
        print(f"It's {player_name}'s TURN!")
        user_input = input(self.get_move_message())
        return user_input
