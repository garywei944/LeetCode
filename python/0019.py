from leetcode_tester import Tester
from src.list_node import ListNode

from typing import Optional, List


class Solution:
    # # 2 pass Approach, find the length first
    # def removeNthFromEnd(
    #         self, head: Optional[ListNode], n: int
    # ) -> Optional[ListNode]:
    #     c, node = 0, head
    #     while node:
    #         node = node.next
    #         c += 1
    #
    #     if c == 1:
    #         return None
    #     elif c == n:
    #         return head.next
    #
    #     n = c - n
    #
    #     node = head
    #     for _ in range(n - 1):
    #         node = node.next
    #     node.next = node.next.next
    #
    #     return head

    # 1 pass Approach, find the length first
    def removeNthFromEnd(
            self, head: Optional[ListNode], n: int
    ) -> Optional[ListNode]:
        slow = fast = head

        for _ in range(n):
            fast = fast.next

        if fast is None:
            return head.next

        fast = fast.next
        while fast is not None:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return head

    # # Recursive and Re-construct Approach, I don't like this approach b/c it
    # # re-constructs every node.
    # def removeNthFromEnd(
    #         self, head: Optional[ListNode], n: int
    # ) -> Optional[ListNode]:
    #     def remove(node):
    #         if node is None:
    #             return 0, None
    #         i, node.next = remove(node.next)
    #         return i + 1, (node, node.next)[i + 1 == n]
    #
    #     return remove(head)[1]

    # # Recursive Approach
    # def removeNthFromEnd(
    #         self, head: Optional[ListNode], n: int
    # ) -> Optional[ListNode]:
    #     def index_remove(node):
    #         if node is None:
    #             return 0
    #         i = index_remove(node.next) + 1
    #         if i == n + 1:
    #             node.next = node.next.next
    #         return i
    #
    #     start = ListNode(0, head)
    #
    #     index_remove(start)
    #
    #     return start.next


if __name__ == '__main__':
    solution = Solution()
    test = Tester(solution.removeNthFromEnd)

    test.addTest(
        ListNode.from_list([1, 2, 3, 4, 5]), 2,
        ListNode.from_list([1, 2, 3, 5])
    )
    test.addTest(
        ListNode.from_list([1]), 1,
        None
    )
    test.doTest()

    # print(solution.removeNthFromEnd(ListNode.from_list([1, 2, 3, 4, 5]), 2))
