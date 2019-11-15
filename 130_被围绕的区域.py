class Solution:
    # 解法1 dfs
    def solve(self, board: List[List[str]]) -> None:
        """
            对每一个边界O进行dfs，dfs将每个连通的O先置#
            之后遍历 将O翻转为X 将#翻转为O
        """
        if not board or len(board) < 1:return
        m = len(board)
        n = len(board[0])
        def dfs(board,i,j):
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] == 'X' or board[i][j] == '#':
                return
            board[i][j] = '#'
            # 上下左右dfs
            dfs(board,i+1,j)
            dfs(board,i-1,j)
            dfs(board,i,j-1)
            dfs(board,i,j+1)
        for i in range(m):
            for j in range(n):
                if (i == 0 or i == m-1 or j == 0 or j == n - 1) and board[i][j] == 'O':
                    dfs(board,i,j)
        for i in range(m):
            for j in range(n):
                board[i][j] = 'X' if board[i][j] == 'O' else board[i][j]
                board[i][j] = 'O' if board[i][j] == '#' else board[i][j]

