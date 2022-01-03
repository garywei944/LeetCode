"""
Backtracking Approach

Theoretical same search path with DFS, the difference is the cost of  DFS is
way too memory consuming by explicitly maintain the stack and convert from
str to list of list, back and forward.
"""
from leetcode_tester import Tester

from typing import Optional, List, Tuple, Union


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def add(i: int, j: int, x: int):
            board[i][j] = str(x)
            bm_row[i] |= 1 << x
            bm_col[j] |= 1 << x
            bm_sqr[i // 3 * 3 + j // 3] |= 1 << x

        def remove(i: int, j: int, x: int):
            board[i][j] = '.'
            bm_row[i] ^= 1 << x
            bm_col[j] ^= 1 << x
            bm_sqr[i // 3 * 3 + j // 3] ^= 1 << x

        def is_safe(i: int, j: int, x: int) -> bool:
            return not (
                    bm_row[i] & 1 << x or
                    bm_col[j] & 1 << x or
                    bm_sqr[i // 3 * 3 + j // 3] & 1 << x
            )

        def init():
            for i in range(9):
                for j in range(9):
                    if board[i][j] != '.':
                        add(i, j, int(board[i][j]))

        def backtrack(i: int = 0, j: int = 0):
            if i == 9:
                return True

            next_i, next_j = divmod(i * 9 + j + 1, 9)

            if board[i][j] == '.':
                for x in range(1, 10):
                    if is_safe(i, j, x):
                        add(i, j, x)
                        if backtrack(next_i, next_j):
                            return True
                        remove(i, j, x)
            else:
                return backtrack(next_i, next_j)
            return False

        bm_row, bm_col, bm_sqr = [
            [0 for _ in range(9)] for _ in range(3)
        ]

        init()
        backtrack()

        return board


if __name__ == '__main__':
    solution = Solution()
    test = Tester(solution.solveSudoku)

    game = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]

    answer = [
        ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
        ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
        ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
        ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
        ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
        ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
        ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
        ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
        ["3", "4", "5", "2", "8", "6", "1", "7", "9"]
    ]

    # Make a masked sudoku for debug
    import numpy as np
    import copy

    n_masks = 40
    rng = np.random.default_rng(42)
    mask = rng.permutation(81)[:n_masks]
    masked = copy.deepcopy(answer)

    for m in mask:
        r, c = divmod(m, 9)
        masked[r][c] = '.'

    test.addTest(
        masked, answer
    )
    test.addTest(
        game, answer
    )
    # test.doTest()

    # result = solution.solveSudoku(game)
    #
    # print('|'.join([''.join(r) for r in result]))

    hard_game = [
        [".", ".", "9", "7", "4", "8", ".", ".", "."],
        ["7", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", "2", ".", "1", ".", "9", ".", ".", "."],
        [".", ".", "7", ".", ".", ".", "2", "4", "."],
        [".", "6", "4", ".", "1", ".", "5", "9", "."],
        [".", "9", "8", ".", ".", ".", "3", ".", "."],
        [".", ".", ".", "8", ".", "3", ".", "2", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "6"],
        [".", ".", ".", "2", "7", "5", "9", ".", "."]
    ]

    hard_answer = [
        ["5", "1", "9", "7", "4", "8", "6", "3", "2"],
        ["7", "8", "3", "6", "5", "2", "4", "1", "9"],
        ["4", "2", "6", "1", "3", "9", "8", "7", "5"],
        ["3", "5", "7", "9", "8", "6", "2", "4", "1"],
        ["2", "6", "4", "3", "1", "7", "5", "9", "8"],
        ["1", "9", "8", "5", "2", "4", "3", "6", "7"],
        ["9", "7", "5", "8", "6", "3", "1", "2", "4"],
        ["8", "3", "2", "4", "9", "1", "7", "5", "6"],
        ["6", "4", "1", "2", "7", "5", "9", "8", "3"]
    ]

    test.addTest(
        hard_game, hard_answer
    )
    test.doTest()
    print(solution.solveSudoku(hard_game))
