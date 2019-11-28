# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None or head.next is None or head.next.next is None:return None
        slow,fast = head.next,head.next.next
        while fast and fast.next and fast.next.next:
            if slow == fast:break
            slow = slow.next
            fast = fast.next.next
        cur = head
        if not fast or not fast.next or not fast.next.next:
            return None
        while slow != cur:
            slow = slow.next
            cur = cur.next
        return cur