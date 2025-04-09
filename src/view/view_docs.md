# View - How it Looks
**Description**: How should we show the state to the user?

## What it concerns:
1. **Command Line Interface:**
    0. Print prompt for user to start the game

    1. Prompt user for single or multiplayer

    2. Prompt user for Difficulty Level (if multiplayer)

    3. Prompt first user for Symbol of choice

    1a. Print Game Header

    1b. Display grid
        1b1. Menu
        1b2. Current

    1c. Print Player's Turn
    1c1. Print Player's Scores

    1d. Print winner/ tie

    1e. Print prompt to continue playing

2. **Pygame GUI:**
    1a. Display Game Start Page, with retro TIC TAC TOE, some color, and a button to start

    1b. Change views to Select Between Multiplayer and Single Player
        1b1. Change views to Select Level of Difficulty

    1c. Give Player Choice of Symbol (just the first user)

    1d. Start the Game in a new window to show current grid
        1d0. Show the player's turn at the bottom of the screen
        1d1. Grid box color should change upon hover
        1d2. Mark the selected box with symbol
        1d3. Show player scores also at the bottom of the screen

    1e. Show final state after win or tie side by side with winner announcement

    1f. Ask to replay