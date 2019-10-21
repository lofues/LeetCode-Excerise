class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        n = len(candidates)
        def helper(idx,temp,temp_list):
            if idx > n or temp > target:
                return
            if temp == target and temp_list not in res:
                res.append(temp_list)
                return
            for i in range(idx,n):
                if temp + candidates[i] > target:
                    break
                helper(i+1,temp+candidates[i],temp_list+[candidates[i]])
        helper(0,0,[])
        return res