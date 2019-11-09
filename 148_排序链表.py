# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        left, right = self.devide(head)
        left = self.sortList(left)
        right = self.sortList(right)
        dummyhead = self.merge(left, right)
        return dummyhead

    def devide(self, head: ListNode):
        if head is None:
            return None, None
        slow, fast = head, head.next
        while fast is not None and fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        left, right = head, slow.next
        slow.next = None
        return left, right

    def merge(self, left, right):
        dummyhead = ListNode(None)
        tail = dummyhead
        while left is not None and right is not None:
            if left.val <= right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next
        tail.next = left if left is not None else right
        return dummyhead.next
