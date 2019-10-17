class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        while nums1:
            flag = True
            x = nums1.pop(0)
            index = nums2.index(x)
            for v in nums2[index:]:
                if v > x:
                    result.append(v)
                    flag = False
                    break
            if flag: result.append(-1)
        return result