import random

def calculate_medium_move(possible_moves: list, state_dimension: int) -> int:
        
    dim = state_dimension
    corners = [0, int(dim - 1), int(dim * (dim - 1)), int((dim + 1) * (dim - 1))]
    
    if dim % 2 == 0:
        center_top_left = (corners[0] + corners[-1]) // 2
        center_bottom_left = center_top_left + dim
        center = [center_top_left, center_top_left + 1, center_bottom_left, center_bottom_left + 1]
    
    else:
        center = [(corners[0] + corners[-1]) // 2]

    corners_plus_center = corners + center
    choices = [str(index + 1) for index in corners_plus_center]
    random.shuffle(choices)
    
    for choice in choices:
        if choice in possible_moves:
            move = int(choice)
            return move
            
    choice_str = random.choice(possible_moves)
    move = int(choice_str)
    return move    
    

possible_moves = [str(i) for i in range(1, 17)]
dim = 4

expected = [i for i in range(1, 17)]

for i in range(50):
    move = calculate_medium_move(possible_moves, dim)
    if move not in expected:
        print("Unexpected: ", move)
    else:
        print("Expected: ", move)

print("Done!")