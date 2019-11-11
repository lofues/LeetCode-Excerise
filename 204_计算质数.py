class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1:return 0
        from math import sqrt
        temp = [True for i in range(n)]
        temp[0],temp[1] =False,False
        for num in range(2,int(sqrt(n)+1)):
            if temp[num] == False:
                continue
            for j in range(num*2,n,num):
                temp[j] = False
        return temp.count(True)