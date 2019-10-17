class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        for index in range(len(A)):
            if A[index] % 2 == 0:
                A.insert(0,A.pop(index))
        return A