from leetcode_tester import Tester
from src.list_node import ListNode

from typing import Optional, List


# # One pass and re-construct Approach
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         r = []
#         while head is not None:
#             r.append(head.val)
#             head = head.next
#
#         head = None
#         for e in r:
#             head = ListNode(e, head)
#
#         return head


# # Recursive Approach
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if head is None or head.next is None:
#             return head
#
#         node = self.reverseList(head.next)
#
#         head.next.next = head
#         head.next = None
#
#         return node


# Iterative Approach
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr is not None:
            node = curr.next
            curr.next = prev

            prev, curr = curr, node
        return prev


if __name__ == '__main__':
    solution = Solution()
    test = Tester(solution.reverseList)

    test.addTest(
        ListNode.from_list([1, 2, 3, 4, 5]),
        ListNode.from_list([5, 4, 3, 2, 1])
    )
    test.addTest(
        ListNode.from_list([1, 2]),
        ListNode.from_list([2, 1])
    )
    test.addTest(
        ListNode.from_list([]),
        ListNode.from_list([])
    )
    test.doTest()

    # print(solution.reverseList(ListNode.from_list([1, 2, 3, 4, 5])))
