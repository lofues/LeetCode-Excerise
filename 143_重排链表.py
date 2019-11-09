# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return head
        slow,fast = head,head.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        right = None
        left,cur = head,slow.next
        slow.next = None
        # 头插法创建右半部分链表
        while cur is not None:
            cur_next = cur.next
            cur.next = right
            right = cur
            cur = cur_next
        dummyhead = ListNode(None)
        tail = dummyhead
        while left is not None and right is not None:
            left_next,right_next = left.next,right.next
            tail.next = left
            tail = tail.next
            tail.next = right
            tail = tail.next
            left,right = left_next,right_next
        tail.next = left if left is not None else right
        return dummyhead.next