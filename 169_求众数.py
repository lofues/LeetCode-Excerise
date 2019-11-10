class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        cancadite = None
        for num in nums:
            if count == 0:
                cancadite = num
            count += 1 if num != cancadite else -1
        return cancadite