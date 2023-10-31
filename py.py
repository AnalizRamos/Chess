def create_board():
    board = []
    for i in range(8):
        row = []
        for j in range(8):
            row.append(get_piece(i, j))
        board.append(row)
    return board
def get_piece(row, col):
    if row < 1 or row > 6:
        return ''
    if col < 0 or col > 7:
        return ''

    if row % 2 == 0:
        if col % 2 == 0:
            if row < 2:
                return 'P'
            else:
                return ''
        else:
            if row == 7:
                return 'p'
            else:
                return ''
    else:
        if col % 2 == 0:
            if row == 6:
                return 'p'
            else:
                return ''
        else:
            if row < 2:
                piece = ['', 'N', 'B', '', 'Q', '', 'B', 'N']
                return piece[col]
            else:
                piece = ['', 'n', 'b', '', 'q', '', 'b', 'n']
                return piece[col]
def is_valid_move(row, col):
    if row < 0 or row > 7 or col < 0 or col > 7:
        return False
    return True
def get_user_move(board):
    move = []
    while True:
        try:
            print("\nEnter your move (start row, start column, destination row, destination column):")
            start_row, start_col, dest_row, dest_col = map(int, input().split())
            if is_valid_move(start_row, start_col) and is_valid_move(dest_row, dest_col):
                move.append((start_row, start_col, dest_row, dest_col))
                break
            else:
                print("Invalid move. Please enter a valid move.")
        except ValueError:
            print("Invalid input. Please enter numbers.")
    return move
def display_board(board):
    for row in board:
        print(" ".join(row))
def run_game():
    board = create_board()
    display_board(board)
    while True:
        move = get_user_move(board)
        if not move:
            break
        # Process the move here. For now, we'll just print the move.
        print("You made the move:", move[0])
        