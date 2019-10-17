class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        if len(arr1) == len(arr2) == 0 or len(arr1) == len(arr2) == 1: return arr1
        i,j = 0,0
        for k in range(len(arr2)):
            for j in range(i,len(arr1)):
                if k >= 1:
                    if arr2[k] == arr2[k-1]: break
                if arr1[j] == arr2[k]:
                    arr1[i], arr1[j] = arr1[j], arr1[i]
                    i += 1
        arr1[i:] = sorted(arr1[i:])
        return arr1