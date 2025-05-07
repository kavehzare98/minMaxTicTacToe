def display_grid(state : list, state_name : str) -> None:
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


def test():

    cases = [
        ['X', 'O', 'X', 'X', 'O', 'O', 'O', 'X', 'X'],  # Full board, no winner
        ['X', 'O', 'X', 'O', 'X', '-', 'O', 'X', 'O'],  # Almost full, no winner
        ['-', '-', '-', '-', '-', '-', '-', '-', '-'],  # Empty board
    ]

    menu = [str(num) for num in range(1, 5)]

    for case in cases:
        display_grid(case, "CURRENT")

    display_grid(menu, "MENU")
    
test()