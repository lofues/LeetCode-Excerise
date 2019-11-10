# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        hash_table = {headA,}
        while headA is not None:
            hash_table.add(headA)
            headA = headA.next
        while headB is not None:
            if headB in hash_table:
                return headB
            headB = headB.next
        return None