class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = collections.defaultdict(list)
        for string in strs:
            ans[tuple(sorted(string))].append(string)
        return ans.values()