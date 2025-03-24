board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
    ]

def display_board(board):
    print('\n TIC TAC TOE')
    print('***************')
    for row in board:
        print('* '+' | '.join(row) + " *")
        print('***************')

display_board(board)


def player_input(player):
    print(f"Player {player}'s turn...")
    row = int(input('Enter row (0,1,2): '))
    column = int(input('Enter column (0,1,2): '))
    board[row][column]=player

player_input('X')
display_board(board)

def check_win(board, player):
    for row in board:
        if row.count(player) == 3:
            return True

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True

    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False