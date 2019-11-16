class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        ret = []
        min_len, max_len = float('inf'), float('-inf')
        # 找出单词的最大和最小长度
        for word in wordDict:
            if len(word) < min_len: min_len = len(word)
            if len(word) > max_len: max_len = len(word)

        def helper(s, word_dict, ans, ret, min_len, max_len):
            if not s:
                ret.append(ans)
                return
            if len(s) >= min_len:
                for i in range(max_len,min_len-1,-1):
                    if len(s) >= i and  s[:i] in word_dict:
                        temp = ans + s[:i] if not ans else ans + ' ' + s[:i]
                        helper(s[i:], word_dict, temp, ret, min_len, max_len)

        helper(s, wordDict, '', ret, min_len, max_len)
        return ret

a = Solution()
print(a.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))