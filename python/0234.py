from leetcode_tester import Tester
from src.list_node import ListNode

from typing import Optional, List


# # List Approach
# class Solution:
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         l_ = []
#         while head is not None:
#             l_.append(head.val)
#             head = head.next
#
#         n = len(l_)
#         for i in range(n // 2):
#             if l_[i] != l_[n - i - 1]:
#                 return False
#
#         return True

# # Recursive Approach
# # Note that it still use O(n) space b/c it creates n recursive stacks
# class Solution:
#     def __init__(self):
#         self.head = None
#
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         self.head = head
#
#         def recursive_check(node):
#             if node is not None:
#                 if not recursive_check(node.next):
#                     return False
#
#                 if node.val != self.head.val:
#                     return False
#                 self.head = self.head.next
#             return True
#
#         return recursive_check(head)

# Reverse Approach
# Reverse the first half and compare it with the second half
# I don't think we should care about immutability, otherwise we don't want to
# modify the linked list anyway.
# https://leetcode.com/problems/palindrome-linked-list/discuss/64500/11-lines-12-with-restore-O(n)-time-O(1)-space
class Solution:
    def isPalindrome(self, head):
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next
        while rev and rev.val == slow.val:
            slow = slow.next
            rev = rev.next
        return not rev


if __name__ == '__main__':
    solution = Solution()
    test = Tester(solution.isPalindrome)

    test.addTest(
        ListNode.from_list([1, 2, 2, 1]),
        True
    )
    test.addTest(
        ListNode.from_list([1, 2]),
        False
    )
    test.doTest()

    # print(solution.isPalindrome(
    #     ListNode.from_list([1, 2, 2, 1])
    # ))
