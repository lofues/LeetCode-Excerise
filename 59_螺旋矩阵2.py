class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n < 1: return []
        matrix = [[None for _ in range(n)] for i in range(n)]
        start = 1
        def generate_matrix(depth,start):
            nrow,ncol = n - 2 * depth,n- 2*depth
            if nrow <= 0 or ncol <=0:return
            if nrow == 1:
                matrix[depth][depth] = start
                return
            if ncol == 1:
                matrix[depth][depth] =start
                return
            matrix[depth][depth:depth+ncol-1] = [_ for _ in range(start,start+ncol-1)]
            start += ncol-1
            for r in range(depth,depth+nrow-1):
                matrix[r][n-depth-1] = start
                start += 1
            matrix[n-depth-1][depth+1:depth+ncol] = list(reversed(range(start,start+ncol-1)))
            start += ncol-1
            for r in range(depth+nrow-1,depth,-1):
                matrix[r][depth] = start
                start += 1
            generate_matrix(depth+1,start)
        generate_matrix(0,1)
        return matrix