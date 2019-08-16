class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        even,odd = [],[]
        for i in range(len(A)):
            if A[i] % 2== 0:
                even.append(A[i])
            else:
                odd.append(A[i])
        A[0::2] = even
        A[1::2] = odd
        return A