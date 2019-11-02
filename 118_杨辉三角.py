class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ret = []
        for i in range(1,numRows+1):
            if i == 1:
                ret.append([1])
            elif i == 2:
                ret.append([1,1])
            else:
                tmp = [1] + [ret[-1][_-1]+ret[-1][_]  for _ in range(1,i-1)] + [1]
                ret.append(tmp)
        return ret