import math

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print("| " + " | ".join(row) + " |")
    print()

# Mapping 1-9 to the corresponding (row, col) positions
position_mapping = {
    1: (0, 0), 2: (0, 1), 3: (0, 2),
    4: (1, 0), 5: (1, 1), 6: (1, 2),
    7: (2, 0), 8: (2, 1), 9: (2, 2)
}

# Function to check for available moves
def available_moves(board):
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                moves.append((i, j))
    return moves

# Function to check if the board is full (draw)
def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

# Function to check if there's a winner
def check_winner(board, player):
    win_conditions = [
        # Horizontal
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        # Vertical
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        # Diagonal
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]]
    ]
    
    return [player, player, player] in win_conditions

# Function for the AI move using the Minimax algorithm
def minimax(board, depth, is_maximizing):
    if check_winner(board, 'O'):
        return 1  # AI wins
    if check_winner(board, 'X'):
        return -1  # Human wins
    if is_board_full(board):
        return 0  # Draw

    if is_maximizing:
        best_score = -math.inf
        for move in available_moves(board):
            board[move[0]][move[1]] = 'O'
            score = minimax(board, depth + 1, False)
            board[move[0]][move[1]] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for move in available_moves(board):
            board[move[0]][move[1]] = 'X'
            score = minimax(board, depth + 1, True)
            board[move[0]][move[1]] = ' '
            best_score = min(score, best_score)
        return best_score

# Function for AI's turn
def ai_move(board):
    best_score = -math.inf
    best_move = None
    for move in available_moves(board):
        board[move[0]][move[1]] = 'O'
        score = minimax(board, 0, False)
        board[move[0]][move[1]] = ' '
        if score > best_score:
            best_score = score
            best_move = move
    board[best_move[0]][best_move[1]] = 'O'

# Function for the human's turn
def human_move(board):
    while True:
        try:
            move = int(input("Enter a number (1-9) for your move: "))
            if move in position_mapping:
                row, col = position_mapping[move]
                if board[row][col] == ' ':
                    board[row][col] = 'X'
                    break
                else:
                    print("That spot is already taken! Try again.")
            else:
                print("Invalid input. Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Main function to play the game
def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]  # 3x3 Tic-Tac-Toe board
    print("Welcome to Tic-Tac-Toe! You are 'X' and the AI is 'O'.")
    print("Here's the board layout:")
    print(" 1 | 2 | 3 ")
    print("---|---|---")
    print(" 4 | 5 | 6 ")
    print("---|---|---")
    print(" 7 | 8 | 9 ")
    print_board(board)
    
    while True:
        # Human's move
        human_move(board)
        print_board(board)
        
        if check_winner(board, 'X'):
            print("You win!")
            break
        if is_board_full(board):
            print("It's a draw!")
            break
        
        # AI's move
        ai_move(board)
        print_board(board)
        
        if check_winner(board, 'O'):
            print("The AI wins!")
            break
        if is_board_full(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()
