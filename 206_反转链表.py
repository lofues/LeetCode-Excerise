# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        reversed_list = ListNode(-1)
        cur = head
        while cur != None:
            temp = cur
            cur = cur.next
            temp.next = reversed_list.next
            reversed_list.next = temp
        return reversed_list.next