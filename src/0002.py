# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        r = ListNode(0, ListNode())
        temp = r
        cache = 0
        while l1 is not None or l2 is not None:
            temp.next = ListNode()
            temp = temp.next
            a = l1.val if l1 is not None else 0
            b = l2.val if l2 is not None else 0
            n = cache + a + b
            temp.val = n % 10
            cache = n // 10
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
        if cache != 0:
            temp.next = ListNode(cache, None)
        r = r.next
        return r
