BISHOP_NORMALIZED_MOVES = set([(1, 1), (1, -1), (-1, 1), (-1, -1)])
QUEEN_NORMALIZED_MOVES = set([(1, 0), (-1, 0), (0, -1),
    (0, 1), (1, 1), (1, -1), (-1, 1), (-1, -1)])
ROOK_NORMALIZED_MOVES = set([(1, 0), (-1, 0), (0, -1),
    (0, 1)])
KING_MOVES = set([(1, 0), (-1, 0), (0, -1),
    (0, 1), (1, 1), (1, -1), (-1, 1), (-1, -1)])
KNIGHT_MOVES = set([(-2, 1), (-2, -1), (2, 1), (2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)])
PAWN_MOVES = set([(-1, 0)]) # TODO: Handle pawn directionality
# Map of piece_type -> (piece_moves, moves_are_normalized)
MOVE_DICTIONARY = {'B': (BISHOP_NORMALIZED_MOVES, True), 'Q': (QUEEN_NORMALIZED_MOVES, True),
 'R': (ROOK_NORMALIZED_MOVES, True), 'K': (KING_MOVES, False), 'H': (KNIGHT_MOVES, False), 'P': (PAWN_MOVES, False)}

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
def find_piece(board):
    place = None
    for row_index, row in enumerate(board):
        for column_index, value in enumerate(row):
            if value != 'X':
                place = row_index, column_index
    return place

def is_valid_move(board, file, rank):
    """
    Returns true if the move is a valid move given the board.
    """
    # Fix all the inputs that use is_valid_move
    target_place = get_target_indices(len(board), file, rank)
    place = find_piece(board)
    move_required = target_place[0] - place[0], target_place[1] - place[1]
    piece_correct_moves, normalized = MOVE_DICTIONARY[board[place[0]][place[1]]]
    if normalized:
        return normalize_move(move_required) in piece_correct_moves
    return move_required in piece_correct_moves

def get_valid_moves(board):
    available_moves = []
    file = 'A'
    position = find_piece(board)
    for _ in range(len(board)):
        for j in range(len(board)):
            rank = j + 1
            row_index, column_index = get_target_indices(len(board), file, rank)
            if position[0] == row_index and position[1] == column_index:
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
    position = find_piece(board)
    piece_variable = board[position[0]][position[1]]
    board[position[0]][position[1]] = 'X'
    new_row, new_column = get_target_indices(len(board), file, rank)
    board[new_row][new_column] = piece_variable

def create_board(size, user_piece_input):
    l = []
    for _ in range(size):
        row = []
        for _ in range(size):
            row.append('X')
        l.append(row)
    l[size - 1][0] = user_piece_input
    return l

def validate_user_input(user_input):
    return len(user_input) == 2

def main():
    print('Enter board size!')
    user_board_input = input()
    print('Enter a piece!')
    user_piece_input = input()
    board = create_board(int(user_board_input), user_piece_input)
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