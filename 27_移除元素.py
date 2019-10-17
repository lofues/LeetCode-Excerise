class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ls = len(nums)
        if ls == 0: return ls
        pos = 0
        for i in range(ls):
            if nums[i] == val:
                continue
            else:
                nums[pos] = nums[i]
                pos += 1
        return pos