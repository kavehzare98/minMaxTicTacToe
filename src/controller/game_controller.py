
class GameController:
    def __init__(self, game, player, view):
        self.game = game
        self.player = player
        self.view = view
        self.running = False

    # Input validation
    def get_first_char(self, raw_input: str) -> str:
        lower_input = raw_input.lower()
        first_char = lower_input[0]
        return first_char
    
    def get_start_flag(self, valid_response: str) -> bool:
        start = False
        if valid_response == 'y':
            start = True
        return start
    
    def run(self):
        self.running = True

        while (self.running):
            
    
    

        
