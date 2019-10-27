class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        NROW, NCOL = len(matrix), len(matrix[0])

        def helper(depth):sta
            nrow, ncol = NROW - 2 * depth, NCOL - 2 * depth
            if nrow <= 0 or ncol <= 0: return []
            if nrow == 1: return matrix[depth][depth:depth + ncol]
            if ncol == 1: return [matrix[r][depth] for r in range(depth, depth + nrow)]

            res = []
            res += matrix[depth][depth:depth + ncol - 1]
            res += [matrix[r][depth + ncol - 1] for r in range(depth, depth + nrow - 1)]
            res += reversed(matrix[depth + nrow - 1][depth + 1:depth + ncol])
            res += [matrix[r][depth] for r in reversed(range(depth + 1, depth + nrow))]
            return res + helper(depth + 1)

        return helper(0)