from leetcode_tester import Tester

from typing import Optional, List


class Solution:
    # # Mask array
    # def isValidSudoku(self, board: List[List[str]]) -> bool:
    #     rows = [[False for _ in range(9)] for _ in range(9)]
    #     cols = [[False for _ in range(9)] for _ in range(9)]
    #     boxes = [[False for _ in range(9)] for _ in range(9)]
    #
    #     for i, row in enumerate(board):
    #         for j, n in enumerate(row):
    #             if n != '.':
    #                 n = int(n) - 1
    #                 i_box = i // 3 * 3 + j // 3
    #                 if rows[i][n] or cols[j][n] or boxes[i_box][n]:
    #                     return False
    #                 rows[i][n] = True
    #                 cols[j][n] = True
    #                 boxes[i_box][n] = True
    #     return True

    # Bitmap
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = len(board)

        rows = [0] * N
        cols = [0] * N
        boxes = [0] * N

        for i, row in enumerate(board):
            for j, n in enumerate(row):
                if n != '.':
                    n = int(n) - 1
                    i_box = i // 3 * 3 + j // 3
                    if rows[i] & (1 << n) \
                            or cols[j] & (1 << n) \
                            or boxes[i_box] & (1 << n):
                        return False
                    rows[i] |= 1 << n
                    cols[j] |= 1 << n
                    boxes[i_box] |= 1 << n
        return True


if __name__ == '__main__':
    solution = Solution()
    test = Tester(solution.isValidSudoku)

    test.addTest(
        [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]], True
    )
    test.addTest(
        [["8", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]], False
    )
    test.doTest()
