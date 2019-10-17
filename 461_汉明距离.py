class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x1 = bin(x).replace('0b', '')
        y1 = bin(y).replace('0b', '')
        if len(x1) > len(y1):
            y1 = (len(x1) - len(y1)) * '0' + y1
        else:
            x1 = (len(y1) - len(x1)) * '0' + x1
        cnt = 0
        for i in range(len(x1)):
            if x1[i] != y1[i]:
                cnt += 1
        return cnt

