import random

class TicTacToe:
    def __init__(self):
        self.board = [' '] * 9
        self.current_player = 'X'
        self.computer_player = 'O'

    def print_board(self):
        for i in range(0, 9, 3):
            print(self.board[i], '|', self.board[i + 1], '|', self.board[i + 2])
            if i < 6:
                print("---------")

    def is_winner(self, player):
        # Check rows, columns, and diagonals for a winner
        for i in range(3):
            if all(self.board[i * 3 + j] == player for j in range(3)) or \
               all(self.board[j * 3 + i] == player for j in range(3)):
                return True
        if all(self.board[i] == player for i in [0, 4, 8]) or \
           all(self.board[i] == player for i in [2, 4, 6]):
            return True
        return False

    def is_full(self):
        return ' ' not in self.board

    def is_game_over(self):
        return self.is_winner('X') or self.is_winner('O') or self.is_full()

    def get_available_moves(self):
        return [i for i in range(9) if self.board[i] == ' ']

    def make_move(self, position):
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            self.switch_player()

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def minimax(self, depth, is_maximizing):
        if self.is_winner('X'):
            return -1
        if self.is_winner('O'):
            return 1
        if self.is_full():
            return 0

        if is_maximizing:
            best_score = float('-inf')
            for move in self.get_available_moves():
                self.make_move(move)
                score = self.minimax(depth + 1, False)
                self.board[move] = ' '
                best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for move in self.get_available_moves():
                self.make_move(move)
                score = self.minimax(depth + 1, True)
                self.board[move] = ' '
                best_score = min(score, best_score)
            return best_score

    def find_best_move(self):
        best_score = float('-inf')
        best_move = None

        for move in self.get_available_moves():
            self.make_move(move)
            score = self.minimax(0, False)
            self.board[move] = ' '

            if score > best_score:
                best_score = score
                best_move = move

        return best_move

def main():
    game = TicTacToe()

    while not game.is_game_over():
        game.print_board()

        if game.current_player == 'X':
            position = int(input("Enter your move (1-9): ")) - 1
            if position not in game.get_available_moves():
                print("Invalid move. Try again.")
                continue
        else:
            print("Computer's move:")
            position = game.find_best_move()
            print(position + 1)

        game.make_move(position)

    game.print_board()

    if game.is_winner('X'):
        print("You win!")
    elif game.is_winner('O'):
        print("Computer wins!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    main()