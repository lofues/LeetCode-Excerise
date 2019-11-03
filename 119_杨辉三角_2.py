class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ret = [1]
        for i in range(1,rowIndex+1):
            ret.insert(0,0)
            for j in range(len(ret)-1):
                ret[j] = ret[j] + ret[j+1]
        return ret