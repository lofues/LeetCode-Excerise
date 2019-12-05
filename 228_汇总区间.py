class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ret = []
        temp = []
        for num in nums:
            if not temp or num - temp[-1] == 1:
                temp.append(num)
            else:
                if len(temp) > 1:
                    ret.append('{}->{}'.format(temp[0],temp[-1]))
                else:
                    ret.append('%d'%temp[0])
                temp = [num]
        if temp:
            if len(temp) > 1:
                ret.append('{}->{}'.format(temp[0],temp[-1]))
            else:
                ret.append('%d'%temp[0])
        return ret