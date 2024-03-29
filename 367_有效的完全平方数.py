class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 0 : return False
        low,high = 0,num
        while low <= high:
            mid = low + (high - low) // 2
            if mid * mid == num:
                return True
            elif mid * mid < num:
                low = mid + 1
            else:
                high = mid - 1
        return False