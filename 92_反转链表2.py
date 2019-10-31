# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        pre, cur = None, head
        cnt = 1
        while cnt != m:
            cnt += 1
            pre = cur
            cur = cur.next
        first = cur
        last, n_next = cur, cur.next
        while cnt != n:
            cnt += 1
            last, n_next = n_next, n_next.next
        if pre is not None:
            pre.next = last
        new_head = head if pre is not None else last
        while cur != n_next:
            cur_next = cur.next
            cur.next, pre = pre, cur
            cur = cur_next
        first.next = n_next
        return new_head
