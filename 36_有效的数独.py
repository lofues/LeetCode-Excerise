class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if len(board) != 9 or len(board[0]) != 9:
            return False
        if not self.is_valid_row(board):
            return False
        if not self.is_valid_column(board):
            return False
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not self.is_valid_square(board, i, j):
                    return False
        return True

    def is_valid_row(self, board):
        for i in range(len(board)):
            tmp = [_ for _ in board[i] if _ != '.']
            if len(tmp) != len(set(tmp)):
                return False
        return True

    def is_valid_column(self, board):
        for i in range(len(board)):
            test = [board[_][i] for _ in range(len(board)) if board[_][i] != '.']
            if len(test) != len(set(test)):
                return False
        return True

    def is_valid_square(self, board, i, j):
        test = []
        for k in range(i, i + 3):
            for l in range(j, j + 3):
                if board[k][l] != '.':
                    test.append(board[k][l])
        if len(test) != len(set(test)):
            return False
        return True


