from leetcode_tester import Tester
from src.list_node import ListNode

from typing import Optional, List


# # Iterative Approach
# class Solution:
#     def mergeTwoLists(
#             self, list1: Optional[ListNode], list2: Optional[ListNode]
#     ) -> Optional[ListNode]:
#         head = ListNode(0)
#         tail = head
#
#         while list1 is not None and list2 is not None:
#             if list1.val > list2.val:
#                 tail.next = list2
#                 list2 = list2.next
#             else:
#                 tail.next = list1
#                 list1 = list1.next
#             tail = tail.next
#
#         tail.next = list1 if list1 is not None else list2
#
#         return head.next


# Recursive Approach
class Solution:
    def mergeTwoLists(
            self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1

        if list1.val > list2.val:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
        else:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1


if __name__ == '__main__':
    solution = Solution()
    test = Tester(solution.mergeTwoLists)

    test.addTest(
        ListNode.from_list([1, 2, 4]),
        ListNode.from_list([1, 3, 4]),
        ListNode.from_list([1, 1, 2, 3, 4, 4])
    )
    test.addTest(
        ListNode.from_list([]),
        ListNode.from_list([]),
        ListNode.from_list([])
    )
    test.addTest(
        ListNode.from_list([]),
        ListNode.from_list([0]),
        ListNode.from_list([0])
    )
    test.doTest()
