class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        cnt = 0
        s = set()
        for item in emails:
            pre,post = item.split('@')
            pre = pre.replace('.','')
            if '+' not in pre:
                s.add(pre+'@'+post)
            else:
                s.add(pre.split('+')[0]+'@'+post)
        return len(s)