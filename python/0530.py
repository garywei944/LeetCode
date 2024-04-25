# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
# def traverse(self, node:ListNode):
#     if node is None:
#         return float('inf'), -float('inf'), float('inf')

#     al, bl, rl = self.traverse(node.left)
#     ar, br, rr = self.traverse(node.right)

#     a = min(node.val, al, ar)
#     b = max(node.val, bl, br)
#     r = min(abs(node.val-bl), abs(node.val-ar), rl, rr)

#     return a, b, r

# def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
#     a, b, r = self.traverse(root)

#     return r
from itertools import pairwise


class Solution:
    def traverse(self, node: ListNode):
        if node is None:
            return
        self.traverse(node.left)
        self.arr.append(node.val)
        self.traverse(node.right)

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.arr = []
        self.traverse(root)
        print(self.arr)
        ans = float("inf")
        for a, b in pairwise(self.arr):
            ans = min(ans, b - a)

        return ans
