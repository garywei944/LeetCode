from typing import Optional, Union, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_

    def __str__(self):
        result = f'{self.val}'
        if self.next:
            result = f'{result} -> {self.next}'
        return result

    def __eq__(self, node):
        if not isinstance(node, self.__class__):
            return False
        return self.val == node.val and self.next == node.next

    @classmethod
    def from_list(cls, values: Union[List[int], int]) -> Optional['ListNode']:
        if not values:
            return None
        if not isinstance(values, list):
            return ListNode(values)

        r = None
        for e in values[::-1]:
            r = ListNode(e, r)

        return r
