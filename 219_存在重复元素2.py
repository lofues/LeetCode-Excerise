class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) <= 1:return False
        elif k <= 0: return False
        hashmap = {}
        for i,num in enumerate(nums):
            if num not in hashmap:
                hashmap[num] = i
            else:
                if i - hashmap[num] <= k:
                    return True
                else:
                    hashmap[num] = i
        return False
