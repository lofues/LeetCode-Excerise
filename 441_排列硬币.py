class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        low,high = 0,n
        while low <= high:
            mid = low + (high-low)//2
            if (mid+1)*mid/2 <= n and (mid+2)*(mid+1)/2 >n:
                return mid
            elif (mid+1)*mid/2 >n:
                high = mid-1
            else:
                low = mid + 1