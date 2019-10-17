class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = 0, x
        while high - low > 1e-6:
            mid = low + (high - low) / 2
            if mid * mid < x:
                low = mid
            elif mid * mid > x:
                high = mid
            else:
                return int(mid)
        return int(high)


