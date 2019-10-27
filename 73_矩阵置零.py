class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        queue = []
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    queue.append((i, j))
        tmp_row = [0 for _ in range(n)]
        while queue:
            row, col = queue.pop(0)
            matrix[row][:] = tmp_row
            for pos in range(m):
                matrix[pos][col] = 0
