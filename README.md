# LeetCode

My LeetCode profile: [garywei944](https://leetcode.com/garywei944/)

## Update for 2023

I start to do LeetCode in the web page using original interface for pure OA
experience.
So only some of the **medium** or **hard** problems are maintained in this
repo.
Checkout my LeetCode profile for more!

## Python3

### Tester

I use [Devgum/leetcode_tester](https://github.com/Devgum/leetcode_tester) to
test codes locally.

```shell
pip install leetcode-tester
```

### Data Structures

All data structures supports `XXXXX.from_list()` to quickly create instance
from list. e.g.

```python
ListNode.from_list([2, 4, 3])
```

creates a linked list of `2 -> 4 -> 3 -> None`.

#### Linked List (ListNode)

```python
from src.list_node import ListNode
```

```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_
```

#### Binary Tree (TreeNode)

LeetCode uses level-order traverse(BFS order) to represent a Binary Tree.

```python
from src.binary_tree import TreeNode, null
```

```python
# Definition for a binary tree other.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

## Problem Tracks

| Number | Name                                                                                                    | Difficulty | Solution                  | Time       | Space | Notes                                    |
|--------|---------------------------------------------------------------------------------------------------------|------------|---------------------------|------------|-------|------------------------------------------|
| 0002   | [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)                                       | Medium     | [python3](python/0002.py) | O(n)       | O(n)  |                                          |
| 0007   | [Reverse Integer](https://leetcode.com/problems/reverse-integer/)                                       | Medium     | [python3](python/0007.py) | O(log x)   | O(1)  |                                          |
| 0008   | [String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/)                       | Medium     | [python3](python/0008.py) | O(n)       | O(1)  | Regex                                    |
| 0019   | [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)     | Medium     | [python3](python/0019.py) | O(n)       | O(1)  | One pass by using 2 pointers             |
| 0036   | [Valid Sudoku](https://leetcode.com/problems/valid-sudoku/)                                             | Medium     | [python3](python/0036.py) | O(n^2)     | O(n)  | Bitmap for less space. n=9               |
| 0037   | [Sudoku Solver](https://leetcode.com/problems/sudoku-solver/)                                           | Hard       | [python3](python/0037.py) | O((9!)^9)  | O(n)  | Backtrack, use 3 bitmaps. n=9, OJ 305 ms |
| 0038   | [Count and Say](https://leetcode.com/problems/count-and-say/)                                           | Medium     | [python3](python/0038.py) | O(2^(n+1)) | O(n)  |                                          |
| 0048   | [Rotate Image](https://leetcode.com/problems/rotate-image/)                                             | Medium     | [python3](python/0048.py) | O(n^2)     | O(1)  | Transpose then reflect via y-axis        |
| 0098   | [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)               | Medium     | [python3](python/0098.py) | O(n)       | O(n)  |                                          |
| 0102   | [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)   | Medium     | [python3](python/0102.py) | O(n)       | O(n)  |                                          |
| 0122   | [Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/) | Medium     | [python3](python/0122.py) | O(n)       | O(1)  |                                          |
| 0189   | [Rotate Array](https://leetcode.com/problems/rotate-array/)                                             | Medium     | [python3](python/0189.py) | O(n)       | O(1)  | Reverse array, O(n) swaps                |
