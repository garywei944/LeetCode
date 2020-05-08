# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        r = ListNode()
        temp = r
        while(l1 is not None and l2 is not None):
        	temp.val = l1 + l2
        	temp.next = ListNode()
        	if temp.val > 9:
        		temp.val %= 10
        		temp.next.val = 1
            l1 = l1.next
            l2 = l2.next
            temp = temp.next
        if l1 is None:
        	temp.next = l2
        else:
        	temp.next = l1
