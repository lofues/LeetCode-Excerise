class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        num_l = []
        for num in range(left,right+1):
            flag = True
            temp = num
            while num != 0:
                i = num % 10
                if i == 0:
                    flag = False
                    break
                elif temp % i != 0:
                    flag = False
                    break
                num //= 10
            if flag:
                num_l.append(temp)
        return num_l