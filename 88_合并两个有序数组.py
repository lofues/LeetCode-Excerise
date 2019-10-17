class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:m + n] = nums2
        for i in range(m, m + n):
            x = nums1[i]
            j = i - 1
            while j >= 0 and nums1[j] > x:
                nums1[j + 1] = nums1[j]
                j -= 1
            nums1[j + 1] = x
