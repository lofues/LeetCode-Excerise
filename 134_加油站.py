class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 贪心算法
        # 记录total 表示循环的差值之和，若total<0则返回-1
        # 记录一个从start开始的sum和 循环更新
        start,total  = 0, 0
        cur_sum = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if cur_sum < 0:
                start = i
                cur_sum = gas[i] - cost[i]
            else:
                cur_sum += gas[i] - cost[i]
        return -1 if total < 0 else start