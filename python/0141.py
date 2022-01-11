from leetcode_tester import Tester
from src.list_node import ListNode

import sys

from typing import Optional, List


# MAX = 100001
#
#
# # Non-immutable approach, change node value in place everytime
# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         while head is not None:
#             if head.val == MAX:
#                 return True
#             head.val = MAX
#             head = head.next
#
#         return False

# # Record reference approach
# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         r = {}
#         while head is not None and id(head) not in r:
#             r[id(head)] = None
#             head = head.next
#
#         return head is not None


# # Python dirty hack, 5 comes empirical
# # An explanation from https://leetcode.com/problems/linked-list-cycle/discuss/44494/Except-ionally-fast-Python/423332
# # * 1 ref comes from the calling of this function itself according to the documentation
# # * 2 Refs from the object being created, compiled and stored for optimization
# # * 1 ref from a node A's next
# # * 1 ref comes from another node B's next [if this happens, then there is a cycle]
# class Solution:
#     def hasCycle(self, head):
#         while sys.getrefcount(head) < 5:
#             head = head.next
#         return bool(head)


# Floyd's Cycle Finding Algorithm
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast, slow = head, head

        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next

            if slow is fast:
                return True

        return False

    def tester(self, head, pos):
        if pos == -1 or head is None:
            return self.hasCycle(head)

        node, tail = head, head

        while tail is not None and tail.next is not None:
            tail = tail.next

        for _ in range(pos):
            node = node.next

        tail.next = node

        return self.hasCycle(head)


if __name__ == '__main__':
    solution = Solution()
    test = Tester(solution.tester)

    # test.addTest(
    #     ListNode.from_list([3, 2, 0, -4]), 1, True
    # )
    # test.addTest(
    #     ListNode.from_list([1, 2]), 0, True
    # )
    # test.addTest(
    #     ListNode.from_list([1]), -1, False
    # )
    # test.doTest()

    print(solution.tester(ListNode.from_list([3, 2, 0, -4]), 1))
