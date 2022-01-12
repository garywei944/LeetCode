from collections import deque
from typing import List, Union, Optional

NULL = 'null'
null = NULL


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        """
        Level order traverse
        """
        s = []
        q = deque()
        q.append(self)
        while len(q) > 0:
            node = q.popleft()
            if node is None:
                s.append(NULL)
            else:
                s.append(str(node.val))
                q.append(node.left)
                q.append(node.right)

        while s[-1] == NULL:
            s.pop()

        return str(s)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (
                    self.val == other.val and
                    self.left == other.left and
                    self.right == other.right
            )
        return False

    @classmethod
    def from_list(
            cls, values: List[Union[int, str, None]]
    ) -> Optional['TreeNode']:
        """
        Construct tree from level order traverse
        """
        if values is None:
            return None

        nodes = [
            TreeNode(e) if e is not None and e != NULL else None
            for e in values
        ]
        reverse = nodes[::-1]
        root = reverse.pop()

        for node in nodes:
            if node is not None:
                if len(reverse) > 0:
                    node.left = reverse.pop()
                if len(reverse) > 0:
                    node.right = reverse.pop()

        return root
