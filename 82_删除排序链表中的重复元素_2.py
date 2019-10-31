# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        slow,fast = dummy,head
        dummy.next = head
        while fast is not None:
            if fast.next is not None and fast.next.val == fast.val:
                tmp = fast.val
                while fast is not None and tmp == fast.val:
                    fast = fast.next
            else:
                slow.next = fast
                slow = fast
                fast = slow.next
        slow.next = fast
        return dummy.next