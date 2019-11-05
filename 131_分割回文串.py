class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # 采用回溯算法，搜索遍历并判断
        if not s: return []
        elif len(s) == 1:return [s]
        ret = []
        length = len(s)
        def is_palindrome(string):
            return string == string[::-1]
        def helper(ans,s,i):
            if i == length:
                ret.append(ans)
                return
            for index in range(i,length):
                tmp = s[i:index+1]
                if is_palindrome(tmp):
                    helper(ans+[tmp],s,index+1)
        helper([],s,0)
        return ret