from leetcode_tester import Tester
from python.src.list_node import ListNode


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

    # For test use
    def tester(self, head, node):
        self.deleteNode(node)

        return head


if __name__ == '__main__':
    solution = Solution()

    test = Tester(solution.tester)

    head = ListNode.from_list([4, 5, 1, 9])
    node = head.next  # 5
    test.addTest(
        head, node, ListNode.from_list([4, 1, 9])
    )

    head = ListNode.from_list([4, 5, 1, 9])
    node = head.next.next  # 1
    test.addTest(
        head, node, ListNode.from_list([4, 5, 9])
    )
    test.doTest()
