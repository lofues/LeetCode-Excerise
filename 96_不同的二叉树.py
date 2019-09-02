class Solution:
    def numTrees(self, n: int) -> int:
        if n < 0:
            return 0
        ret = [0]*(n+1)
        if n == 1:
            return 1
        elif n == 2:
            return 2
        ret[0],ret[1],ret[2] = 1,1,2
        for i in range(2,n+1):
            ret[i] = sum(ret[j-1]*ret[i-j] for j in range(1,i+1))
        return ret[n]