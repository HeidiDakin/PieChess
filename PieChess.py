# Today, we want to end with a functioning 2x2 game board and queen.

# [Row Change, Column Change]
# Since we print later rows lower, [1, 0] is down.

QUEEN_NORMALIZED_MOVES = set([(1, 0), (-1, 0), (0, -1),
    (0, 1), (1, 1), (1, -1), (-1, 1), (-1, -1)])

def normalize_move(move):
    assert move[0] != 0 or move[1] != 0
    if abs(move[0]) >= abs(move[1]):
        return move[0]/abs(move[0]), move[1]/abs(move[0])
    if abs(move[1]) > abs(move[0]):
        return move[0]/abs(move[1]), move[1]/abs(move[1])
    # (x, y) = (x/ max|(x, y)|, y/ max|(x, y))
    # return the normalized move

def get_target_indices(board_size, file, rank):
    # given file and rank, find the board indices of a move.
    row = board_size - rank
    column = ord(file) - ord('A')
    return row, column

# Hint - You might want to make your board a 2D list.
def find_queen(board):
    queen_place = None
    for row_index, row in enumerate(board):
        for column_index, value in enumerate(row):
            if value == 'Q':
                queen_place = row_index, column_index
    return queen_place

def is_valid_move(board, file, rank):
    """
    Returns true if the move is a valid move given the board.
    """
    # Fix all the inputs that use is_valid_move
    target_place = get_target_indices(len(board), file, rank)
    queen_place = find_queen(board)
    move_required = target_place[0] - queen_place[0], target_place[1] - queen_place[1]
    return normalize_move(move_required) in QUEEN_NORMALIZED_MOVES

def get_valid_moves(board):
    available_moves = []
    file = 'A'
    queen_position = find_queen(board)
    for _ in range(len(board)):
        for j in range(len(board)):
            rank = j + 1
            row_index, coloumn_index = get_target_indices(len(board), file, rank)
            if queen_position[0] == row_index and queen_position[1] == coloumn_index:
                continue
            if is_valid_move(board, file, rank):
                available_moves.append(f'{file}{rank}')
        file = chr(ord(file[0]) + 1)
    return ', '.join(available_moves)

def print_board(board):
    header_string = '    '
    char = 'A'
    underscore_string = '    '
    for i in range(len(board)):
        header_string += char + ' '
        underscore_string += '_ '
        new_char = ord(char[0])
        new_char += 1
        char = chr(new_char)
    print(header_string)
    print(underscore_string)
    for i in range(len(board)):
        rank = len(board) - i
        print(f'{rank} | ', end = '')
        for j in range(len(board[0])):
            print(board[i][j], end = ' ')
        print()

def apply_move(board, file, rank):
    assert is_valid_move(board, file, rank)
    queen_position = find_queen(board)
    board[queen_position[0]][queen_position[1]] = 'X'
    new_row, new_column = get_target_indices(len(board), file, rank)
    board[new_row][new_column] = 'Q'

def create_board(size):
    l = []
    for _ in range(size):
        row = []
        for _ in range(size):
            row.append('X')
        l.append(row)
    l[0][0] = 'Q'
    return l

def validate_user_input(user_input):
    return not len(user_input) > 2

def main():
    print('Enter board size!')
    user_board_input = input()
    board = create_board(int(user_board_input))
    print("Welcome to PieChess!")
    print_board(board)
    while True:
        print(f'Enter your move! Available moves - {get_valid_moves(board)}')
        user_input = input()
        if user_input == 'quit':
            return
        if not validate_user_input(user_input):
            print('Please enter move in correct format, ex: B3')
            continue
        file = user_input[0]
        rank = int(user_input[1])
        if not is_valid_move(board, file, rank):
            print('Please enter a valid move!')
            continue
        apply_move(board, file, rank)
        print_board(board)

if __name__ == "__main__":
    main()