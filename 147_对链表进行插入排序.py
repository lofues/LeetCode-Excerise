# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        cur = dummy = ListNode(None)
        while head:
            while cur.next and cur.next.val <= head.val:
                cur = cur.next
            temp = head
            head = head.next
            temp.next = cur.next
            cur.next = temp

            cur = dummy
        return dummy.next
