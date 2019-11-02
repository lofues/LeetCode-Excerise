# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        tmp = []
        while head is not None:
            tmp.append(head.val)
            head = head.next
        def generate_tree(nums):
            if not nums: return None
            index = len(nums)//2
            root = TreeNode(nums[index])
            root.left = generate_tree(nums[:index])
            root.right = generate_tree(nums[index+1:])
            return root
        root = generate_tree(tmp)
        return root