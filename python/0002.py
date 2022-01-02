from leetcode_tester import Tester, ListNode

from typing import List, Optional


# Definition for singly-linked list.
# class ListNode:
#
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def add_one(a, b, r):
    t = a + b + r
    return t % 10, t // 10


def add_other(a, r):
    return add_one(a, 0, r)


class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> \
            Optional[ListNode]:
        rem = 0
        results = []

        while l1 is not None and l2 is not None:
            curr, rem = add_one(l1.val, l2.val, rem)
            results.append(curr)

            l1 = l1.next
            l2 = l2.next

        node = l2 if l1 is None else l1

        while node is not None:
            curr, rem = add_other(node.val, rem)
            results.append(curr)

            node = node.next

        if rem != 0:
            results.append(rem)

        result = None
        for r in results[::-1]:
            result = ListNode(r, result)

        return result


if __name__ == '__main__':
    solution = Solution()
    test = Tester(solution.addTwoNumbers)

    test.addTest(
        [2, 4, 3], [5, 6, 4],
        [7, 0, 8]
    )
    test.doTest()
