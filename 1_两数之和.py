class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        _dict = {}
        for i, v in enumerate(nums):
            _dict[v] = i
        for i, num in enumerate(nums):
            result = target - num
            if result in _dict:
                j = _dict[result]
                if j != i:
                    return [i, j]

