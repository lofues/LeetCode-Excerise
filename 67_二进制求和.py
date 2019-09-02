class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a,b = '0b'+a,'0b'+b
        res = int(a,2) + int(b,2)
        return bin(res)[2:]