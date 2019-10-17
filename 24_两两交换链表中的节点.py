# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummyhead = ListNode(-1)
        dummyhead.next = head
        prev,p = dummyhead,head
        while p and p.next:
            q,r = p.next,p.next.next
            prev.next = q
            p.next = r
            q.next = p
            prev = p
            p = r
        return dummyhead.next