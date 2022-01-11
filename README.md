# LeetCode

My LeetCode profile: [garywei944](https://leetcode.com/garywei944/)

## Python3

### Tester

I use [Devgum/leetcode_tester](https://github.com/Devgum/leetcode_tester) to
test codes locally.

```shell
pip install leetcode-tester
```

### Data Structures

#### ListNode

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

## Problem Tracks

| Number | Name                                                                                                      | Difficulty | Solution                  | Time        | Space | Notes                                                                                                     |
|--------|-----------------------------------------------------------------------------------------------------------|------------|---------------------------|-------------|-------|-----------------------------------------------------------------------------------------------------------|
| 0001   | [Two Sum](https://leetcode.com/problems/two-sum/)                                                         | Easy       | [python3](python/0001.py) | O(n)        | O(n)  | Hash Function                                                                                             |
| 0002   | [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)                                         | Medium     | [python3](python/0002.py) | O(n)        | O(n)  |                                                                                                           |
| 0007   | [Reverse Integer](https://leetcode.com/problems/reverse-integer/)                                         | Medium     | [python3](python/0007.py) | O(log_10 x) | O(1)  |                                                                                                           |
| 0008   | [String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/)                         | Medium     | [python3](python/0008.py) | O(n)        | O(1)  | Regex                                                                                                     |
| 0014   | [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)                             | Easy       | [python3](python/0014.py) | O(n S)      | O(1)  | S: the length of shortest input string                                                                    |
| 0019   | [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)       | Medium     | [python3](python/0019.py) | O(n)        | O(1)  | One pass by using 2 pointers                                                                              |
| 0021   | [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)                           | Easy       | [python3](python/0021.py) | O(n)        | O(1)  |                                                                                                           |
| 0026   | [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) | Easy       | [python3](python/0026.py) | O(n)        | O(1)  |                                                                                                           |
| 0028   | [Implement strStr()](https://leetcode.com/problems/implement-strstr/)                                     | Easy       | [python3](python/0028.py) | O(n)        | O(1)  |                                                                                                           |
| 0036   | [Valid Sudoku](https://leetcode.com/problems/valid-sudoku/)                                               | Medium     | [python3](python/0036.py) | O(n^2)      | O(n)  | Bitmap for less space. n=9                                                                                |
| 0037   | [Sudoku Solver](https://leetcode.com/problems/sudoku-solver/)                                             | Hard       | [python3](python/0037.py) | O((9!)^9)   | O(n)  | Backtrack, use 3 bitmaps. n=9, OJ 305 ms                                                                  |
| 0038   | [Count and Say](https://leetcode.com/problems/count-and-say/)                                             | Medium     | [python3](python/0038.py) | O(2^(n+1))  | O(n)  |                                                                                                           |
| 0048   | [Rotate Image](https://leetcode.com/problems/rotate-image/)                                               | Medium     | [python3](python/0048.py) | O(n^2)      | O(1)  | Transpose then reflect via y-axis                                                                         |
| 0066   | [Plus One](https://leetcode.com/problems/plus-one/)                                                       | Easy       | [python3](python/0066.py) | O(n)        | O(1)  |                                                                                                           |
| 0122   | [Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)   | Medium     | [python3](python/0122.py) | O(n)        | O(1)  |                                                                                                           |
| 0125   | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)                                       | Easy       | [python3](python/0125.py) | O(n)        | O(1)  | Regex                                                                                                     |
| 0136   | [Single Number](https://leetcode.com/problems/single-number/)                                             | Easy       | [python3](python/0136.py) | O(n)        | O(1)  | XOR                                                                                                       |
| 0141   | [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)                                     | Easy       | [python3](python/0141.py) | O(n)        | O(1)  | Use Floyd's Cycle Finding Algorithm. sys.getrefcount() also works surprisingly                            |
| 0189   | [Rotate Array](https://leetcode.com/problems/rotate-array/)                                               | Medium     | [python3](python/0189.py) | O(n)        | O(1)  | Reverse array, O(n) swaps                                                                                 |
| 0206   | [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)                                 | Easy       | [python3](python/0206.py) | O(n)        | O(1)  |                                                                                                           |
| 0234   | [Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)                           | Easy       | [python3](python/0234.py) | O(n)        | O(1)  | Reverse the first half linked list, then compare                                                          |
| 0237   | [Delete Node in a Linked List](https://leetcode.com/problems/delete-node-in-a-linked-list/)               | Easy       | [python3](python/0237.py) | O(1)        | O(1)  |                                                                                                           |
| 0242   | [Valid Anagram](https://leetcode.com/problems/valid-anagram/)                                             | Easy       | [python3](python/0242.py) | O(n)        | O(1)  | Sorted Approach take O(n log n) time, O(1) space, but should be faster. Counter Approach takes O(n) time. |
| 0283   | [Move Zeros](https://leetcode.com/problems/move-zeroes/)                                                  | Easy       | [python3](python/0283.py) | O(n)        | O(1)  |                                                                                                           |
| 0344   | [Reverse String](https://leetcode.com/problems/reverse-string/)                                           | Easy       | [python3](python/0344.py) | O(n)        | O(1)  |                                                                                                           |
| 0350   | [Intersection of Two Arrays II](https://leetcode.com/problems/intersection-of-two-arrays-ii/)             | Easy       | [python3](python/0350.py) | O(n)        | O(n)  |                                                                                                           |
| 0387   | [First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string/)   | Easy       | [python3](python/0387.py) | O(n)        | O(n)  |                                                                                                           |
