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

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.val == other.val and self.next == other.next
        return False

    @classmethod
    def from_list(cls, values: Union[List[int], int]) -> Optional['ListNode']:
        if values is None:
            return None
        if not isinstance(values, list):
            return cls(values)

        r = None
        for e in values[::-1]:
            r = cls(e, r)

        return r
