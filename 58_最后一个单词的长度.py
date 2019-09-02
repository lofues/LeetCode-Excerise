class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s or s == ' ':
            return 0
        s = re.findall(r'\S+',s)
        if s:
            return len(s[-1])
        else:
            return 0