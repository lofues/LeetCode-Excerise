class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        dic = collections.Counter(a+b for a in A for b in B)
        return sum(dic.get(-1*(c+d),0) for c in C for d in D)