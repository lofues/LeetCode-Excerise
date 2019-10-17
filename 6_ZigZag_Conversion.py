class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # 找出计算规律
        if len(s) == 1 or numRows==1: return s
        res = ''
        for row in range(1,numRows+1):
            cur = row - 1
            if row == 1:
                res += s[cur:len(s):2*(numRows-row)]
            elif row == numRows:
                res += s[cur:len(s):2*(numRows-1)]
            else:
                flag = True
                while cur < len(s):
                    res += s[cur]
                    if flag:
                        cur+=(numRows-row) * 2
                        flag = False
                    else:
                        cur +=(row-1) * 2
                        flag = True
        return res