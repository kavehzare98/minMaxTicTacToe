import unittest
from Model.Game import Game

class TestGame(unittest.TestCase):
    """
    Unit tests for the Game class in the Tic Tac Toe application.
    This test suite verifies board extraction methods, state updates,
    move validation, and overall game status (win/draw/reset).
    """

    # =========================
    # HELPER METHODS FOR BOARD EXTRACTION
    # =========================

    # def run_get_rows_test(self, dim=3):
    #     """
    #     Helper function to test get_rows() for a board of dimension dim x dim.
    #     Verifies that the method correctly extracts rows from the internal 1D state.
    #     """
    #     game = Game(dim)
    #     game.set_current_state(game.get_menu_state())
    #     rows = game.get_rows()
    #     expected_rows = [[str(dim * r + c + 1) for c in range(dim)] for r in range(dim)]
    #     self.assertEqual(rows, expected_rows)
    
    # def test_get_rows_cases(self):
    #     """
    #     Parameterized test for get_rows() across board dimensions 2 to 9.
    #     """
    #     for i in range(2, 10):
    #         self.run_get_rows_test(i)

    # def run_get_cols_test(self, dim=3):
    #     """
    #     Helper function to test get_cols() which extracts columns from the 1D state.
    #     """
    #     game = Game(dim)
    #     game.set_current_state(game.get_menu_state())
    #     cols = game.get_cols()
    #     expected_cols = [[str(dim * r + c + 1) for r in range(dim)] for c in range(dim)]
    #     self.assertEqual(cols, expected_cols)

    # def test_get_cols_cases(self):
    #     """
    #     Parameterized test for get_cols() across board dimensions 2 to 9.
    #     """
    #     for i in range(2, 10):
    #         self.run_get_cols_test(i)

    # def run_get_diags_test(self, dim=3):
    #     """
    #     Tests the diagonals returned by get_diags() for a board of dimension dim.
    #     Verifies both the main (top-left to bottom-right) and anti-diagonal.
    #     """
    #     game = Game(dim)
    #     game.set_current_state(game.get_menu_state())
    #     back_diag, forward_diag = game.get_diags()

    #     expected_backward_diagonal = [str(i * (dim + 1) + 1) for i in range(dim)]
    #     expected_forward_diagonal = [str((i + 1) * (dim - 1) + 1) for i in range(dim)]

    #     self.assertEqual(back_diag, expected_backward_diagonal)
    #     self.assertEqual(forward_diag, expected_forward_diagonal)

    # def test_get_diags_cases(self):
    #     """
    #     Parameterized test for get_diags() across board dimensions 2 to 9.
    #     """
    #     for i in range(2, 10):
    #         self.run_get_diags_test(i)

    # # =========================
    # # STATE UPDATE METHODS
    # # =========================

    # def run_update_current_state_test(self, move_pos, move_symbol, dim=3):
    #     """
    #     Tests update_current_state() by making a move and verifying the new board state.
    #     """
    #     n = dim ** 2
    #     game = Game(dim)
    #     game.update_current_state(move_pos, move_symbol)
    #     expected_state = ['-' for _ in range(n)]
    #     expected_state[move_pos - 1] = move_symbol
    #     self.assertEqual(game.get_current_state(), expected_state)

    # def test_update_current_state_cases(self):
    #     """
    #     Tests update_current_state() using all valid positions and both player symbols.
    #     Includes an edge case with move 0 (invalid).
    #     """
    #     test_cases = [(i, 'X') for i in range(1, 10)] + [(i, 'O') for i in range(1, 10)] + [(0, 'X')]
    #     for move_pos, move_symbol in test_cases:
    #         with self.subTest(move=move_pos, symbol=move_symbol):
    #             self.run_update_current_state_test(move_pos, move_symbol)

    # def run_update_possible_moves_test(self, move: int, dim: int = 3):
    #     """
    #     Tests update_possible_moves() by making a move and checking the resulting list of available moves.
    #     """
    #     move_str = str(move)
    #     n = dim ** 2
    #     game = Game(dim)

    #     game.update_possible_moves(move)
    #     new_possible_moves = game.get_possible_moves()
    #     expected_possible_moves = [str(num) for num in range(1, n + 1)]
    #     expected_possible_moves.remove(move_str)

    #     self.assertEqual(new_possible_moves, expected_possible_moves)

    # def test_update_possible_moves_cases(self):
    #     """
    #     Tests update_possible_moves() for all valid positions across board dimensions 2 to 9.
    #     """
    #     for dim in range(2, 10):
    #         for move in range(1, dim ** 2 + 1):
    #             self.run_update_possible_moves_test(move, dim)

    # # =========================
    # # SPECIAL GAME METHODS
    # # =========================

    # def run_validate_move_test(self, move: str, expected_flag: bool, dim: int = 3):
    #     """
    #     Tests validate_move() to ensure it correctly flags legal and illegal moves.
    #     """
    #     game = Game(dim)
    #     actual_flag = game.validate_move(move)
    #     self.assertEqual(actual_flag, expected_flag)

    # def test_validate_move_cases(self):
    #     """
    #     Tests validate_move() across a range of inputs including invalid and valid values.
    #     """
    #     dim = 4
    #     for move in range(25):
    #         expected = 1 <= move <= dim ** 2
    #         self.run_validate_move_test(str(move), str(expected), dim)

    # def run_is_draw_test(self, test_case: list, dim: int = 3):
    #     """
    #     Tests is_draw() by providing a board state and checking if a draw is correctly detected.
    #     """
    #     game = Game(dim)
    #     game.set_current_state(test_case)
    #     expected = '-' not in test_case
    #     self.assertEqual(game.is_draw(), expected)

    # def test_is_draw_cases(self):
    #     """
    #     Tests is_draw() for boards with unfinished games and a full board with no winner.
    #     """
    #     test_cases = [
    #         ['X', 'O', 'X', 'X', 'O', 'X', '-', '-', '-'],
    #         ['-', 'X', 'O', '-', 'X', 'O', 'X', '-', '-'],
    #         ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
    #     ]
    #     for case in test_cases:
    #         self.run_is_draw_test(case)

    def run_is_winner_test(self, new_state: list, expected_flag: bool, dim: int = 3):
        """
        Tests is_winner() by verifying correct win detection for predefined board states.
        """
        p1_symbol = 'X'
        p2_symbol = 'O'
        game = Game(dim)
        game.set_current_state(new_state)
        self.assertEqual(game.check_for_winner(p1_symbol, p2_symbol), expected_flag)

    def test_is_winner_cases(self):
        """
        Tests is_winner() using multiple cases including:
        - no winner scenarios
        - valid win scenarios (rows, columns, diagonals)
        """
        no_winner_cases = [
            ['X', 'O', 'X', 'X', 'O', 'O', 'O', 'X', 'X'],
            ['X', 'O', 'X', 'O', 'X', '-', 'O', 'X', 'O'],
            ['-', '-', '-', '-', '-', '-', '-', '-', '-'],
            ['X', 'O', 'X', '-', 'X', 'O', '-', 'O', '-'],
            ['O', 'X', 'O', 'X', 'O', 'X', '-', '-', '-'],
            ['X', 'O', '-', 'X', '-', 'O', '-', 'X', '-'],
            ['-', 'X', 'O', 'O', '-', 'X', 'X', 'O', '-'],
            ['O', 'X', 'O', 'O', 'X', '-', 'X', 'O', 'X'],
            ['X', 'O', '-', 'O', 'X', 'X', '-', '-', 'O'],
        ]
        winner_cases = [
            ['X', 'X', 'X', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', 'O', 'O', 'O', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', 'X', 'X', 'X'],
            ['O', '-', '-', 'O', '-', '-', 'O', '-', '-'],
            ['-', 'X', '-', '-', 'X', '-', '-', 'X', '-'],
            ['-', '-', 'O', '-', '-', 'O', '-', '-', 'O'],
            ['X', '-', '-', '-', 'X', '-', '-', '-', 'X'],
            ['-', '-', 'O', '-', 'O', '-', 'O', '-', '-'],
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

        for case in no_winner_cases:
            self.run_is_winner_test(case, False)

        for case in winner_cases:
            self.run_is_winner_test(case, True)

    # def run_reset_game_test(self, state: list, winner: str, dim=3):
    #     """
    #     Tests reset_game() by applying it to a game in progress or with a winner,
    #     and checking if the game state, winner, and move list are reset.
    #     """
    #     game = Game(dim)
    #     game.set_current_state(state)
    #     game.set_winner(winner)
    #     game.reset_game()

    #     expected_state = game.get_default_state()
    #     expected_moves = [str(i) for i in range(1, dim**2 + 1)]

    #     self.assertEqual(game.get_current_state(), expected_state)
    #     self.assertEqual(game.get_possible_moves(), expected_moves)
    #     self.assertIsNone(game.get_winner())

    # def test_reset_game_cases(self):
    #     """
    #     Tests reset_game() with a variety of scenarios including games in progress,
    #     finished draws, and games with a winner.
    #     """
    #     all_cases = [
    #         ['X', 'O', 'X', 'X', 'O', 'O', 'O', 'X', 'X'],
    #         ['X', 'O', 'X', 'O', 'X', '-', 'O', 'X', 'O'],
    #         ['-', '-', '-', '-', '-', '-', '-', '-', '-'],
    #         ['X', 'O', 'X', '-', 'X', 'O', '-', 'O', '-'],
    #         ['O', 'X', 'O', 'X', 'O', 'X', '-', '-', '-'],
    #         ['X', 'O', '-', 'X', '-', 'O', '-', 'X', '-'],
    #         ['-', 'X', 'O', 'O', '-', 'X', 'X', 'O', '-'],
    #         ['O', 'X', 'O', 'O', 'X', '-', 'X', 'O', 'X'],
    #         ['X', 'O', '-', 'O', 'X', 'X', '-', '-', 'O'],
    #     ]
    #     winner_cases = [
    #         ['X', 'X', 'X', '-', '-', '-', '-', '-', '-'],
    #         ['-', '-', '-', 'O', 'O', 'O', '-', '-', '-'],
    #         ['-', '-', '-', '-', '-', '-', 'X', 'X', 'X'],
    #         ['O', '-', '-', 'O', '-', '-', 'O', '-', '-'],
    #         ['-', 'X', '-', '-', 'X', '-', '-', 'X', '-'],
    #         ['-', '-', 'O', '-', '-', 'O', '-', '-', 'O'],
    #         ['X', '-', '-', '-', 'X', '-', '-', '-', 'X'],
    #         ['-', '-', 'O', '-', 'O', '-', 'O', '-', '-'],
    #     ]

    #     for case in all_cases:
    #         self.run_reset_game_test(case, None)

    #     for case in winner_cases:
    #         self.run_reset_game_test(case, "Player1")

if __name__ == '__main__':
    unittest.main()