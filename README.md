# LeetCode

[garywei944](https://leetcode.com/garywei944/)

## Python3

### Tester

I use [Devgum/leetcode_tester](https://github.com/Devgum/leetcode_tester) to
test codes locally.

```shell
pip install leetcode-tester
```

### Problem Tracks

| Number | Name                                                                                                      | Difficulty | Time        | Space | Notes                                                                                                     |
|--------|-----------------------------------------------------------------------------------------------------------|------------|-------------|-------|-----------------------------------------------------------------------------------------------------------|
| 0001   | [Two Sum](https://leetcode.com/problems/two-sum/)                                                         | Easy       | O(n)        | O(n)  | Hash Function                                                                                             |
| 0002   | [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)                                         | Medium     | O(n)        | O(n)  ||
| 0007   | [Reverse Integer](https://leetcode.com/problems/reverse-integer/)                                         | Medium     | O(log_10 x) | O(1)  |                                                                                                           |
| 0008   | [String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/)                         | Medium     | O(n)        | O(1)  | Regex                                                                                                     |
| 0014   | [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)                             | Easy       | O(n S)      | O(1)  | S: the length of shortest input string                                                                    |
| 0026   | [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) | Easy       | O(n)        | O(1)  ||
| 0028   | [Implement strStr()](https://leetcode.com/problems/implement-strstr/)                                     | Easy       | O(n)        | O(1)  |                                                                                                           |
| 0036   | [Valid Sudoku](https://leetcode.com/problems/valid-sudoku/)                                               | Medium     | O(n^2)      | O(n)  | Bitmap for less space. n=9                                                                                |
| 0037   | [Sudoku Solver](https://leetcode.com/problems/sudoku-solver/)                                             | Hard       | O((9!)^9)   | O(n)  | Backtrack, use 3 bitmaps. n=9, OJ 305 ms                                                                  |
| 0038   | [Count and Say](https://leetcode.com/problems/count-and-say/)                                             | Medium     | O(2^(n+1))  | O(n)  |                                                                                                           |
| 0048   | [Rotate Image](https://leetcode.com/problems/rotate-image/)                                               | Medium     | O(n^2)      | O(1)  | Transpose then reflect via y-axis                                                                         |
| 0066   | [Plus One](https://leetcode.com/problems/plus-one/)                                                       | Easy       | O(n)        | O(1)  |                                                                                                           |
| 0122   | [Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)   | Medium     | O(n)        | O(1)  ||
| 0125   | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)                                       | Easy       | O(n)        | O(1)  | Regex                                                                                                     |
| 0136   | [Single Number](https://leetcode.com/problems/single-number/)                                             | Easy       | O(n)        | O(1)  | XOR                                                                                                       |
| 0189   | [Rotate Array](https://leetcode.com/problems/rotate-array/)                                               | Medium     | O(n)        | O(1)  | Reverse array, O(n) swaps                                                                                 |
| 0242   | [Valid Anagram](https://leetcode.com/problems/valid-anagram/)                                             | Easy       | O(n)        | O(1)  | Sorted Approach take O(n log n) time, O(1) space, but should be faster. Counter Approach takes O(n) time. |
| 0283   | [Move Zeros](https://leetcode.com/problems/move-zeroes/)                                                  | Easy       | O(n)        | O(1)  |                                                                                                           |
| 0344   | [Reverse String](https://leetcode.com/problems/reverse-string/)                                           | Easy       | O(n)        | O(1)  |                                                                                                           |
| 0350   | [Intersection of Two Arrays II](https://leetcode.com/problems/intersection-of-two-arrays-ii/)             | Easy       | O(n)        | O(n)  |                                                                                                           |
| 0387   | [First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string/)   | Easy       | O(n)        | O(n)  |                                                                                                           |
