from leetcode_tester import Tester
from python.src.list_node import ListNode

from typing import Optional, List


class Solution:
    def removeNthFromEnd(
            self, head: Optional[ListNode], n: int
    ) -> Optional[ListNode]:
        c, node = 0, head
        while node:
            node = node.next
            c += 1

        if c == 1:
            return None
        elif c == n:
            return head.next

        n = c - n

        node = head
        for _ in range(n - 1):
            node = node.next
        node.next = node.next.next

        return head


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
