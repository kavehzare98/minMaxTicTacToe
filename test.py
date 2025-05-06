from src.Model.Game import Game

def test():

    game = Game()

    no_winner_cases = non_winning_cases = [
        ['X', 'O', 'X', 'X', 'O', 'O', 'O', 'X', 'X'],  # Full board, no winner
        ['X', 'O', 'X', 'O', 'X', '-', 'O', 'X', 'O'],  # Almost full, no winner
        ['-', '-', '-', '-', '-', '-', '-', '-', '-'],  # Empty board
        ['X', 'O', 'X', '-', 'X', 'O', '-', 'O', '-'],  # In progress, no win
        ['O', 'X', 'O', 'X', 'O', 'X', '-', '-', '-'],  # Draw in progress
        ['X', 'O', '-', 'X', '-', 'O', '-', 'X', '-'],  # Scattered, no win
        ['-', 'X', 'O', 'O', '-', 'X', 'X', 'O', '-'],  # Random no win
        ['O', 'X', 'O', 'O', 'X', '-', 'X', 'O', 'X'],  # Close game, no win
        ['X', 'O', '-', 'O', 'X', 'X', '-', '-', 'O'],  # In progress, no win
    ]

    # Winner
    winner_cases = winning_cases = [
        # Rows
        ['X', 'X', 'X', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', 'O', 'O', 'O', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', 'X', 'X', 'X'],
        
        # Columns
        ['O', '-', '-', 'O', '-', '-', 'O', '-', '-'],
        ['-', 'X', '-', '-', 'X', '-', '-', 'X', '-'],
        ['-', '-', 'O', '-', '-', 'O', '-', '-', 'O'],
        
        # Diagonals
        ['X', '-', '-', '-', 'X', '-', '-', '-', 'X'],
        ['-', '-', 'O', '-', 'O', '-', 'O', '-', '-'],
        
        # Additional mixed winning cases (alternate symbols, scattered placement)
        ['X', 'X', 'X', 'O', '-', 'O', '-', '-', '-'],
        ['O', 'X', 'X', 'O', 'X', '-', 'O', '-', '-'],
        ['-', 'O', '-', '-', 'O', '-', '-', 'O', 'X'],
        ['X', '-', '-', '-', 'X', 'O', '-', '-', 'X'],
        ['O', '-', 'X', 'O', 'X', '-', 'O', '-', '-'],
        ['-', '-', 'O', '-', 'O', 'X', 'O', '-', '-'],
        ['-', '-', 'X', '-', 'X', 'O', 'X', '-', 'O'],
        ['O', '-', 'O', '-', 'O', '-', 'O', '-', 'X'],
        ['-', '-', '-', '-', '-', '-', 'X', 'X', 'X'],
    ]

    p1_symbol = 'X'
    p2_symbol = 'O'

    winner_flag = False
    case_num = 1
    for case in no_winner_cases:
        game.set_current_state(case)
        flag = game.is_winner(p1_symbol, p2_symbol)
        if winner_flag != flag:
            print(f"NO WINNER: FAILED case number: {case_num}\n", case)
        case_num += 1

    winner_flag = True
    case_num = 1
    for case in winner_cases:
        game.set_current_state(case)
        flag = game.is_winner(p1_symbol, p2_symbol)
        if winner_flag != flag:
            print(f"WINNER: FAILED case number: {case_num}\n", case)
        case_num += 1
    
test()