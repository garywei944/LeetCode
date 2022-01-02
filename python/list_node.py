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
        return self.val.__eq__(node.val) and self.next.__eq__(node.next)

    @classmethod
    def from_list(cls, value_list):
        if not value_list:
            return None
        if not isinstance(value_list, list):
            return ListNode(value_list)

        r = None
        for e in value_list[::-1]:
            r = ListNode(e, r)

        return r
