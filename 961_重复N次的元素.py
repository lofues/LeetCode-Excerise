class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        for item in A:
            if A.count(item) == len(A)/2:
                return item