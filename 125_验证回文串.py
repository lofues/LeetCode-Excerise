class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s: return True
        s =''.join(filter(str.isalnum,s)).lower()
        return s == s[::-1]