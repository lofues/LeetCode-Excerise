class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        return [list(reversed([1 - pixel for pixel in row])) for row in A]
