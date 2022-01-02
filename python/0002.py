from leetcode_tester import Tester
from python.src.list_node import ListNode

from typing import Optional


class Solution:
    def addTwoNumbers(
            self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        carry = 0
        results = []
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            carry, curr = divmod(v1 + v2 + carry, 10)

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            results.append(curr)

        r = None
        for e in results[::-1]:
            r = ListNode(e, r)
        return r


if __name__ == '__main__':
    solution = Solution()
    test = Tester(solution.addTwoNumbers)

    test.addTest(
        ListNode.from_list([2, 4, 3]),
        ListNode.from_list([5, 6, 4]),
        ListNode.from_list([7, 0, 8])
    )
    test.addTest(
        ListNode.from_list([0]),
        ListNode.from_list([0]),
        ListNode.from_list([0])
    )
    test.addTest(
        ListNode.from_list([9, 9, 9, 9, 9, 9, 9]),
        ListNode.from_list([9, 9, 9, 9]),
        ListNode.from_list([8, 9, 9, 9, 0, 0, 0, 1])
    )
    test.doTest()
