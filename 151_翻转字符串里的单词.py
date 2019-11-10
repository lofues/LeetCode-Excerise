class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(list(map(lambda x:x.strip(),s.split()))[::-1])