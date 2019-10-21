class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        res = []
        def helper(idx,tmp,temp_list):
            if idx == n or tmp > target:
                return
            if tmp == target:
                res.append(temp_list)
                return
            for i in range(idx,n):
                if tmp + candidates[i] > target:
                    break
                helper(i,tmp+candidates[i],temp_list+[candidates[i]])
        helper(0,0,[])
        return res