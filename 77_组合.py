class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ret = []
        def backtrack(i,cnt,tmp):
            if cnt == 0:
                ret.append(tmp)
                return
            for j in range(i,n+1):
                backtrack(j+1,cnt-1,tmp+[j])
        backtrack(1,k,[])
        return ret