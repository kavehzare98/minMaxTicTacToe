import unittest
from src.Model.Game import Game

class TestGame(unittest.TestCase):

    # TEST HELPER Functions
    def run_get_rows_test(self, dim=3):
        game = Game(dim)
        game.set_current_state(game.get_menu_state().copy())
        rows = game.get_rows()
        expected_rows = [ [str(dim * r + c + 1) for c in range(dim)] for r in range(dim) ]
        self.assertEqual(rows, expected_rows)
    
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

    def test_get_rows_cases(self):
        for i in range(2, 10):
            self.run_get_rows_test(i)
        

    
        

"""
def get_rows(self) -> list:
        state = self.get_dimension()
        num_cols = int(len(state) ** 0.5)
        rows = [state[i:i+num_cols] for i in range(0, len(state), num_cols)]
        return rows
    
    def get_cols(self) -> list:
        state = self.current_state
        num_cols = self.get_dimension()
        cols = []
        for i in range(num_cols):
            col = []
            for j in range(i, len(state), num_cols):
                col.append(state[j])
            cols.append(col)
        return cols
    
    def get_diags(self) -> list:
        state = self.current_state
        num_cols = self.get_dimension()
        backward_diag = []
        forward_diag = []

        for i in range(1, num_cols + 1):
            backward_diag.append(state[(i - 1) * (num_cols + 1)])
            forward_diag.append(state[i * (num_cols - 1)])

        return (backward_diag, forward_diag)
    
    # SPECIAL METHODS
    def validate_move(self, move : int) -> bool:
        if move in self.possible_moves:
            return True
        return False

    def update_possible_moves(self, move : int) -> None:
        move_str = str(move)
        index = self.possible_moves.index(move_str)
        self.possible_moves.pop(index)
    
    def is_draw(self) -> bool:
        if self.winner == None:
            empty_count = self.current_state.count('-')
            if empty_count == 0:
                return True
        return False

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
