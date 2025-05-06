import unittest
from Model.Game import Game

class TestGame(unittest.TestCase):

    # TEST HELPER Functions
    # ============================================== BEGIN

    # get_rows() unit test function
    def run_get_rows_test(self, dim=3):
        game = Game(dim)
        game.set_current_state(game.get_menu_state())
        rows = game.get_rows()
        expected_rows = [ [str(dim * r + c + 1) for c in range(dim)] for r in range(dim) ]
        self.assertEqual(rows, expected_rows)
    
    # get_rows test cases
    def test_get_rows_cases(self):
        for i in range(2, 10):
            self.run_get_rows_test(i)

    # get_cols() UNIT TEST
    def run_get_cols_test(self, dim=3):
        game = Game(dim)
        game.set_current_state(game.get_menu_state())
        cols = game.get_cols()
        expected_cols = [[str(dim * r + c + 1) for r in range(dim)] for c in range(dim)]
        self.assertEqual(cols, expected_cols)

    # get_cols() TEST CASES
    def test_get_cols_cases(self):
        for i in range(2, 10):
            self.run_get_cols_test(i)

    # get_diags() UNIT TEST
    def run_get_diags_test(self, dim=3):
        game = Game(dim)
        game.set_current_state(game.get_menu_state())
        back_diag, forward_diag = game.get_diags()

        expected_backward_diagonal = [str(i * (dim + 1) + 1) for i in range(dim)]
        expected_forward_diagonal = [str((i + 1) * (dim - 1) + 1) for i in range(dim)]
        
        self.assertEqual(back_diag, expected_backward_diagonal)
        self.assertEqual(forward_diag, expected_forward_diagonal)

    # get_diags() TEST CASES
    def test_get_diags_cases(self):
        for i in range(2, 10):
            self.run_get_diags_test(i)

    # ============================================== END



    # UPDATE METHODS
    # ============================================== BEGIN

    # update_current_state() UNIT TEST
    def run_update_current_state_test(self, move_pos, move_symbol, dim=3):
        n = dim ** 2
        game = Game(dim)
        game.update_current_state(move_pos, move_symbol)
        expected_state = ['-' for _ in range(n)]
        expected_state[move_pos - 1] = move_symbol
        self.assertEqual(game.get_current_state(), expected_state)

    # update_current_state() TEST CASES
    def test_update_current_state_cases(self):
        test_cases = [(i, 'X') for i in range(1, 10)]
        test_cases += [(i, 'O') for i in range(1, 10)]
        test_cases.append((0, 'X'))

        for move_pos, move_symbol in test_cases:
            with self.subTest(move=move_pos, symbol=move_symbol):
                self.run_update_current_state_test(move_pos, move_symbol)

    # def update_possible_moves(self, move : int) -> None:
    #     move_str = str(move)
    #     index = self.possible_moves.index(move_str)
    #     self.possible_moves.pop(index)

    # update_possible_moves() UNIT TEST
    def run_update_possible_moves_test(self, move: int, dim: int=3):
        move_str = str(move)
        n = int(dim ** 2)
        game = Game(dim)

        game.update_possible_moves(move)
        new_possible_moves = game.get_possible_moves()
        expected_possible_moves = [str(num) for num in range(1, n + 1)]
        expected_index = expected_possible_moves.index(move_str)
        expected_possible_moves.pop(expected_index)

        self.assertEqual(new_possible_moves, expected_possible_moves)
    
    # update_possible_moves() TEST CASES
    def test_update_possible_moves_cases(self):
        for dim in range(2, 10):
            n = int(dim ** 2)
            for move in range(1, n + 1):
                self.run_update_possible_moves_test(move, dim)

    # ============================================== END
    


    # SPECIAL METHODS
    # ============================================== BEGIN

    # validate_move() UNIT TEST
    def run_validate_move_test(self, move: int, expected_flag: bool, dim: int=3):
        game = Game(dim)
        actual_flag = game.validate_move(move)
        self.assertEqual(actual_flag, expected_flag)

    # validate_move() TEST CASES
    def test_validate_move_cases(self):
        dim = 4
        n = dim ** 2
        for move in range(25):
            flag = False
            if move >= 1 and move <= int(dim**2):
                flag = True
            
            self.run_validate_move_test(move, flag, dim)

    # is_draw() UNIT TEST
    def run_is_draw_test(self, test_case: list, dim: int=3):
        game = Game(dim)
        game.set_current_state(test_case)
        actual_is_draw = game.is_draw()

        expected_empty_count = test_case.count('-')
        if expected_empty_count == 0:
            expected_is_draw = True
        else:
            expected_is_draw = False
        
        self.assertEqual(actual_is_draw, expected_is_draw)

    # is_draw() TEST CASES
    def test_is_draw_cases(self):
        test_cases = [
            ['X', 'O', 'X', 'X', 'O', 'X', '-', '-', '-'],
            ['-', 'X', 'O', '-', 'X', 'O', 'X', '-', '-'],
            ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
        ]

        for case in test_cases:
            self.run_is_draw_test(case)

    # is_winner() UNIT TEST
    def run_is_winner_test(self, new_state: list, expected_flag: bool, dim: int=3):
        p1_symbol = 'X'
        p2_symbol = 'O'
        game = Game(dim)
        game.set_current_state(new_state)
        actual_flag = game.is_winner(p1_symbol, p2_symbol)
        self.assertEqual(actual_flag, expected_flag)

    # is_winner() TEST CASES
    def test_is_winner_cases(self):
        # No Winners
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

        winner_flag = False
        for case in no_winner_cases:
            self.run_is_winner_test(case, winner_flag)
        
        winner_flag = True
        for case in winner_cases:
            self.run_is_draw_test(case, winner_flag)

    # ============================================== END


"""   

    # DETERMINE WINNER
    def is_winner(self, p1_symbol, p2_symbol) -> bool:
        winning_num = self.get_dimension()
        found_winner = False

        # Call helper functions get lists of rows, columns, and diagonals
        rows = self.get_rows()
        cols = self.get_cols()
        diags = self.get_diags()

        # Check rows for winning condition
        for row in rows:
            if found_winner == False:
                if row.count(p1_symbol) == winning_num:
                    self.winner = p1_symbol
                    found_winner = True
                elif row.count(p2_symbol) == winning_num:
                    self.winner = p2_symbol
                    found_winner = True

        # If winner found, quit function
        if found_winner:
            return found_winner
        
        # Check columns for winning condition
        for col in cols:
            if found_winner == False:
                if col.count(p1_symbol) == winning_num:
                    self.winner = p1_symbol
                    found_winner = True
                elif col.count(p2_symbol) == winning_num:
                    self.winner = p2_symbol
                    found_winner = True
        
        if found_winner:
            return found_winner

        # Check forward and backward diagonals for winning condition
        for diag in diags:
            if found_winner == False:
                if diag.count(p1_symbol) == winning_num:
                    self.winner = p1_symbol
                    found_winner = True
                elif diag.count(p2_symbol) == winning_num:
                    self.winner = p2_symbol
                    found_winner = True

        return found_winner
    
    # RESET GAME
    def reset_game(self) -> None:
        self.current_state = self.default_state.copy()
        self.possible_moves = self.menu_state.copy()
        self.winner = None
    """
