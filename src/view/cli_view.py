
class CommandLineInterface():
    
    def __init__(self):
        self.header = """
=======================
WELCOME TO TIC TAC TOE!
=======================

"""
        self.footer = """
======================
BYE BYE!
======================

"""
    def display_header(self) -> None:
        print(self.header)

    def display_footer(self) -> None:
        print(self.footer)

    def display_grid(self, grid) -> None:
        print("")
        col = 0
        for row in range(3):
            print(f" {grid[row][col]} | {grid[row][col + 1]} | {grid[row][col + 2]}")
            if row != 2:
                print("---+---+---")
        print("")

    def display_player_turn(self, player: str) -> None:
        print(f"\nIt is {player}'s Turn!\n")

    def display_winner(self, player: str) -> None:
        print(f"\n{player} WINS!!!\n")

    def display_tie(self) -> None:
        print("\nIt's a TIE.\n")
  
    def display_scores(self, scores_dict: dict) -> None:
        for key, value in scores_dict.items():
            print(f"{key} Score: {value}")


    # Prompting user
    def prompt_user_to_start_game(self) -> str:
        return input("\nWould you like to START playing (Y or N)?\t")

    def prompt_user_to_continue(self) -> str:
        return input("\nWould you like to continue playing (Y or N)?\t")
    
    def prompt_user_for_game_mode(self) -> str:
        return input("\nWould you like to play?\n\t1. Singleplayer\n\t2. Multiplayer\nYour Choice:\t")
    
    def prompt_user_for_difficulty(self) -> str:
        return input("\nPick a difficulty level:\n\t1. Easy\n\t2. Medium\n\t3. Hard\nYour Choice:\t")

    def prompt_user_for_symbol(self) -> str:
        return input("\nWhat game symbol would you like?\n\t1. X\n\t2. O\nYour Choice:\t")
    