class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted([key ** 2 for key in A])