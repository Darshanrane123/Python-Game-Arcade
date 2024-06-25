import math
import random

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(1,10)]  # Single list to represent 3x3 board
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc (tells us what number corresponds to what box)
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # Check row
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True
        # Check column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        # Check diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]  # left-right diagonal
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]  # right-left diagonal
            if all([spot == letter for spot in diagonal2]):
                return True
        return False


def minimax(position, depth, maximizing_player, alpha, beta):
    if position.current_winner == 'X':
        return -1
    elif position.current_winner == 'O':
        return 1
    elif not position.empty_squares():
        return 0

    if maximizing_player:
        max_eval = -math.inf
        for move in position.available_moves():
            position.make_move(move, 'O')
            eval = minimax(position, depth + 1, False, alpha, beta)
            position.board[move] = ' '  # undo move
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for move in position.available_moves():
            position.make_move(move, 'X')
            eval = minimax(position, depth + 1, True, alpha, beta)
            position.board[move] = ' '  # undo move
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval


def get_computer_move(board):
    best_score = -math.inf
    best_move = None
    alpha = -math.inf
    beta = math.inf
    for move in board.available_moves():
        board.make_move(move, 'O')
        score = minimax(board, 0, False, alpha, beta)
        board.board[move] = ' '  # undo move
        if score > best_score:
            best_score = score
            best_move = move
    return best_move


def play_game():
    combinations = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6] ]
    board = TicTacToe()
    print("Welcome to Tic Tac Toe!")
    board.print_board_nums()
    print("To make a move, enter a number from 0-8 as shown above.")

    while board.empty_squares():
        # if board.current_winner:
        #     print(f"The winner is {board.current_winner}!")
        #     break
        if "X" in board.make_move(square)
        if board.num_empty_squares() == 1:
            print("It's a tie!")
            break

        if board.num_empty_squares() % 2 == 1:  # Computer's turn
            move = get_computer_move(board)
            board.make_move(move, 'O')
            print(f"Computer chose position {move}")
            board.print_board()
        else:  # Player's turn
            valid_move = False
            while not valid_move:
                try:
                    move = int(input("Enter your move (0-8): "))
                    if move in board.available_moves():
                        valid_move = True
                        board.make_move(move, 'X')
                        board.print_board()
                    else:
                        print("Invalid move. That spot is already taken!")
                except ValueError:
                    print("Invalid input. Please enter a number.")

    if not board.current_winner:
        print("It's a tie!")

if __name__ == '__main__':
    play_game()
