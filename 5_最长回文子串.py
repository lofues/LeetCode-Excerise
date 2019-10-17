class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) == 1:
            return s
        max_length, max_str = 0, ''
        for i in range(len(s)):
            for j in range(len(s) - 1, i - 1, -1):
                tmp = s[i:j + 1]
                tmp_length = self.is_palindrome(tmp)
                if tmp_length is not None:
                    if tmp_length > max_length:
                        max_length, max_str = tmp_length, tmp
                    break
        return max_str

    def is_palindrome(self, s: str):
        if not s or s[::-1] != s:
            return None
        else:
            return len(s)