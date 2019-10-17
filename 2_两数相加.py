# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = cur = ListNode(0)
        carry = 0
        while l1 or l2:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            cur.next = ListNode(val % 10)
            cur = cur.next
            carry = val // 10
        if carry > 0:
            cur.next = ListNode(carry)
        return head.next