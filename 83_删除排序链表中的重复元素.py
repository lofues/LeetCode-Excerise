# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        cur = head
        while cur is not None:
            cur_next = cur.next
            while cur_next and cur_next.val == cur.val:
                cur_next = cur_next.next
            cur.next = cur_next
            cur = cur_next
        return head