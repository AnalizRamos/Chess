The game is played on a 2D grid of squares, similar to a checkerboard. Each square on the grid is represented by a pair of coordinates (x, y), where x represents the row and y represents the column.

The objective of the game is to capture all the opponent's pieces by moving your pieces onto their squares. This can be achieved by forming a chain of your pieces, with the last piece in the chain pointing towards the edge of the grid.

The game follows these steps:

a. Initialization: The game sets up the initial state of the board by placing the pieces in their initial positions. Each player starts with a certain number of pieces.

b. Player's turn: Each player takes turns moving their pieces according to the following rules:

Each move consists of sliding a piece along a row or a column to an empty square.
A piece can only move if there is at least one square in the direction of the move.
A player can only move a piece that is within the chain of pieces formed by the player's own color.
The game enforces the rule that a piece must always move at least one square. This rule prevents players from trapping their own pieces against the edge of the grid.
c. Game over: The game ends when one of the following conditions is met:

All of the opponent's pieces have been captured.
Both players have agreed to a draw.
A player is unable to make a valid move.
d. Scoring: The game then assigns a score to each player based on the number of pieces they have captured.

Please note that the implementation details may vary, so the specific implementation should be consulted for an accurate explanation of how the game works. # Chess
