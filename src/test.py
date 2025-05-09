from View.CommandLineView import CommandLineView as CLI

def test():
    # TEST CASE ===== BEGIN
    cli = CLI()
    state = ['X', 'O', 'X', 'O', 'X', '-', 'O', 'X', 'O']
    state_name = "CURRENT"
    p1_name = "Cade"
    p2_name = "Kevin"
    p1_score = 3
    p2_score = 2
    winner_name = "Kevin"
    # TEST CASE ===== END

    cli.display_header()

    start = cli.prompt_to_start()
    print(f"START INPUT:{start}")

    name = cli.prompt_for_name()
    print(f"NAME INPUT: {name}")

    mode = cli.prompt_for_mode()
    print(f"MODE INPUT: {mode}")

    move = cli.prompt_for_move(p1_name)
    print(f"MOVE INPUT: {move}")

    cli.display_grid(state, state_name)
        
    cli.display_scores(p1_name, p1_score, p2_name, p2_score)

    cli.display_winner(winner_name)

    cli.display_tie()

    cli.display_error()

    cli.display_footer()

test()



# ====== DISPLAYS ===========
# !display_header(self) -> None
    


#! display_grid(self, state : list, state_name : str) -> None:

#! display_scores(self, p1_name: str, p1_score: int, p2_name : str, p2_score : int) -> None:

#! display_winner(self, winner_name: str) -> None:

# display_tie(self) -> None:

# display_error(self) -> None:

# !display_footer(self) -> None

    # ====== PROMPTS ===========
#! prompt_to_start(self) -> str:

#! prompt_for_name(self) -> str:

#! prompt_for_mode(self) -> str:
 
#! prompt_for_move(self, player_name: str) -> str:
