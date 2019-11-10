class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for i,num in enumerate(numbers):
            if num not in hashmap:
                hashmap[target-num] = i + 1
            else:
                return [hashmap[num],i+1]
        return []