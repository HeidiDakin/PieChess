# Today, we want to end with a functioning 2x2 game board and queen.

# [Row Change, Column Change]
# Since we print later rows lower, [1, 0] is down.

QUEEN_MOVES = {'D': (1, 0), 'U': (-1, 0), 'L': (0, -1),
    'R': (0, 1), 'DRD': (1, 1), 'DLD': (1, -1),
    'URD': (-1, 1), 'ULD': (-1, -1)}

# Hint - You might want to make your board a 2D list.
def find_queen(board):
    queen_place = None
    for row_index, row in enumerate(board):
        for column_index, value in enumerate(row):
            if value == 'Q':
                queen_place = row_index, column_index
    return queen_place

def is_valid_move(board, move):
    """
    Returns true if the move is a valid move given the board.
    """
    queen_place = find_queen(board) 
    if queen_place[0] + move[0] not in [-1, 2] and queen_place[1] + move[1] not in [-1, 2]:
        return True
    return False

def get_valid_moves(board):
    available_moves = []
    for move_name, move in QUEEN_MOVES.items():
        if is_valid_move(board, move):
            available_moves.append(move_name)
    return ', '.join(available_moves)

def print_board(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(board[i][j], end = ' ')
        print()

def apply_move(board, move):
    assert is_valid_move(board, move)
    queen_position = find_queen(board)
    new_row = queen_position[0] + move[0]
    new_column = queen_position[1] + move[1]
    board[queen_position[0]][queen_position[1]] = 'X'
    board[new_row][new_column] = 'Q'

def main():
    board = [['Q', 'X'],['X', 'X']]
    print("Welcome to PieChess!")
    print_board(board)
    while True:
        print(f'Enter your move! Available moves - {get_valid_moves(board)}')
        user_input = input()
        if user_input == 'quit':
            return
        if user_input not in QUEEN_MOVES or not is_valid_move(board, QUEEN_MOVES[user_input]):
            print('Please enter valid move :)')
            continue
        apply_move(board, QUEEN_MOVES[user_input])
        print_board(board)

if __name__ == "__main__":
    main()