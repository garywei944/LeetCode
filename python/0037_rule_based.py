"""
Rule Based Approach

Not complete, if the solution is not unique or 2 rules doesn't come with unique
choice, it doesn't work
"""
from leetcode_tester import Tester

from typing import Optional, List, Tuple
import copy


def isValidSudoku(board: List[List[str]]) -> bool:
    rows = [0 for _ in range(9)]
    cols = [0 for _ in range(9)]
    boxes = [0 for _ in range(9)]

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


def put_one_by_try(board) -> bool:
    for i in range(9):
        for j in range(9):
            if board[i][j] == '.':
                f = False
                cand = -1
                for n in range(1, 10):
                    board[i][j] = str(n)
                    if isValidSudoku(board):
                        if f:
                            f = False
                            cand = -1
                            board[i][j] = '.'
                            break
                        else:
                            f = True
                            cand = n

                    board[i][j] = '.'
                if f:
                    board[i][j] = str(cand)
                    return True
    return False


def get_chunk_idx(i, j):
    _r = i // 3
    _c = j // 3

    result = []
    for _i in range(3):
        for _j in range(3):
            result.append((_r * 3 + _i, _c * 3 + _j))

    return result


def put_one_by_bitmap(board) -> bool:
    bitmap = [
        [
            [
                True for _ in range(9)
            ] for _ in range(9)
        ] for _ in range(9)
    ]

    # Map False
    for i in range(9):
        for j in range(9):
            if board[i][j] != '.':
                n = int(board[i][j]) - 1
                for k in range(9):
                    bitmap[k][j][n] = False
                    bitmap[i][k][n] = False

                for _r, _c in get_chunk_idx(i, j):
                    bitmap[_r][_c][n] = False

    # Find only True
    for n in range(9):
        for i in range(9):
            row_c, col_c, chunk_c = 0, 0, 0
            row_i, col_i, chunk_i = None, None, None
            for j in range(9):
                if bitmap[i][j][n]:
                    row_c += 1
                    row_i = j
                if bitmap[j][i][n]:
                    col_c += 1
                    col_i = j
            for _r, _c in get_chunk_idx(i // 3 * 3, i % 3 * 3):
                if bitmap[_r][_c][n]:
                    chunk_c += 1
                    chunk_i = (_r, _c)
            if row_c == 1:
                board[i][row_i] = str(n + 1)
                return True
            if col_c == 1:
                board[col_i][i] = str(n + 1)
                return True
            if chunk_i == 1:
                _r, _c = chunk_i
                board[_r][_c] = str(n + 1)
                return True

    return False


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        while put_one_by_try(board) or put_one_by_bitmap(board):
            print('|'.join([''.join(r) for r in board]))

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

    # # Make a masked sudoku for debug
    # import numpy as np
    #
    # n_masks = 60
    # rng = np.random.default_rng(42)
    # mask = rng.permutation(81)[:n_masks]
    # masked = copy.deepcopy(answer)
    #
    # for m in mask:
    #     r, c = divmod(m, 9)
    #     masked[r][c] = '.'
    #
    # test.addTest(
    #     masked, answer
    # )
    # test.addTest(
    #     game, answer
    # )
    # test.doTest()
    #
    # # result = solution.solveSudoku(masked)
    # #
    # # print('|'.join([''.join(r) for r in result]))
    #
    # print(put_one_by_bitmap(masked))

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
