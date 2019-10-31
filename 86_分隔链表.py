# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        less,target = [],[]
        while head is not None:
            if head.val >= x:
                target.append(head)
            else:
                less.append(head)
            head = head.next
        # 将各个列表中的节点连接起来
        for i in range(len(less)-1):
             less[i].next = less[i+1]
        for i in range(len(target)-1):
            target[i].next = target[i+1]
        ret = None
        if less:
            ret = less[0]
            if target:
                less[-1].next = target[0]
                target[-1].next = None
            else:
                less[-1].next = None
        else:
            if target:
                ret = target[0]
                target[-1].next = None
        return ret