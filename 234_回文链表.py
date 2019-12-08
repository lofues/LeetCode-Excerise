# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 方法1
# O(N)的空间复杂度
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:return True
        ret = []
        while head is not None:
            ret.append(head.val)
            head = head.next
        return ret == ret[::-1]


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 方法2
# O(1)的空间复杂度：先采用快慢指针找到左右半链表，然后将其中一个链表进行翻转
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next: return True
        slow, quick = head, head.next
        Rhead = None
        while quick and quick.next:
            temp = slow.next
            slow.next = Rhead
            quick = quick.next.next
            Rhead = slow
            slow = temp
        # 如果是偶数
        if quick:
            quick = slow.next
            slow.next = Rhead
        else:
            quick = slow.next
            slow = Rhead
        while quick is not None:
            if quick.val != slow.val:
                return False
            quick = quick.next
            slow = slow.next
        return True
