class NQueensBacktracking:
    def __init__(self, n):
        self.n = n
        self.board = [[0] * n for _ in range(n)]
        self.solutions = []

    def is_safe(self, row, col):
        # Check if there is a queen in the same column
        for i in range(row):
            if self.board[i][col] == 1:
                return False

        # Check upper left diagonal
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False

        # Check upper right diagonal
        for i, j in zip(range(row, -1, -1), range(col, self.n)):
            if self.board[i][j] == 1:
                return False

        return True

    def solve(self, row=0):
        if row == self.n:
            # Found a solution
            self.solutions.append([row[:] for row in self.board])
            return

        for col in range(self.n):
            if self.is_safe(row, col):
                self.board[row][col] = 1
                self.solve(row + 1)
                self.board[row][col] = 0  # Backtrack

    def get_solutions(self):
        return self.solutions

class NQueensBranchAndBound:
    def __init__(self, n):
        self.n = n
        self.solutions = []

    def is_safe(self, row, col, placement):
        # Check if there is a queen in the same column
        for i in range(row):
            if placement[i] == col or \
                    placement[i] - i == col - row or \
                    placement[i] + i == col + row:
                return False
        return True

    def solve(self, row, placement):
        if row == self.n:
            # Found a solution
            self.solutions.append(placement[:])
            return

        for col in range(self.n):
            if self.is_safe(row, col, placement):
                placement[row] = col
                self.solve(row + 1, placement)

    def branch_and_bound_solve(self):
        placement = [-1] * self.n
        self.solve(0, placement)

    def get_solutions(self):
        return self.solutions

# Example usage for Backtracking
n_queens_backtracking = NQueensBacktracking(4)
n_queens_backtracking.solve()
print("Solutions using Backtracking:")
for solution in n_queens_backtracking.get_solutions():
    for row in solution:
        print(row)
    print()

# Example usage for Branch and Bound
n_queens_branch_and_bound = NQueensBranchAndBound(4)
n_queens_branch_and_bound.branch_and_bound_solve()
print("\nSolutions using Branch and Bound:")
for solution in n_queens_branch_and_bound.get_solutions():
    for i in range(len(solution)):
        print([1 if j == solution[i] else 0 for j in range(len(solution))])
    print()