# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head is None:
            return None
        fast = slow = head
        for i in range(n):
            fast = fast.next
        if fast is None:
            return head.next
        while fast.next is not None:
            fast = fast.next
            slow = slow.next
        cur = slow.next
        slow.next = cur.next
        return head
