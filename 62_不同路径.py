class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [[0 for _ in range(n)] for x in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0:
                    matrix[i][j] = 1
                elif j == 0:
                    matrix[i][j] = 1
                else:
                    matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
        return matrix[m-1][n-1]