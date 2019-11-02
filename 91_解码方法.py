class Solution:
    def numDecodings(self, s: str) -> int:
        tmp = set(list(str(x) for x in range(1,27)))
        # 在末尾多出一个空间置1 用来满足动态方程
        ret = [0 for _ in range(len(s)+1)]
        ret[-1] = 1
        length = len(s)
        for i in range(length-1,-1,-1):
            for cur_length in range(1,3):
                if i+cur_length<= length and  s[i:i+cur_length] in tmp:
                    ret[i] += ret[i+cur_length]
        return ret[0]