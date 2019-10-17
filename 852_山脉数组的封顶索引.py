class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        for index in range(1,len(A)):
            if A[index-1] < A[index] and A[index] > A[index+1]:
                return index