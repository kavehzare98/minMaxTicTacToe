import unittest
from Model.Game import Game

class TestGame(unittest.TestCase):

    def run_update_current_state_test(self, move_pos, move_symbol, dim=3):
        n = dim ** 2
        game = Game(dim)
        game.update_current_state(move_pos, move_symbol)
        expected_state = ['-' for _ in range(n)]
        expected_state[move_pos - 1] = move_symbol
        self.assertEqual(game.get_current_state(), expected_state)

    def test_update_current_state_cases(self):
        test_cases = [(i, 'X') for i in range(1, 10)]
        test_cases += [(i, 'O') for i in range(1, 10)]
        test_cases.append((0, 'X'))

        for move_pos, move_symbol in test_cases:
            with self.subTest(move=move_pos, symbol=move_symbol):
                self.run_update_current_state_test(move_pos, move_symbol)
