"""
DFS approach to the problem

Time Limit exceed.

To reduce number of searches the algorithm try to update the board by fill some
position by the only candidate.
"""
from leetcode_tester import Tester

from typing import Optional, List, Union, Tuple
import copy
import sys


def put_one(board: "Board") -> List[List[str]]:
    matrix = board.tolist()

    for i in range(9):
        for j in range(9):
            if matrix[i][j] == '.':
                f = False
                cand = -1
                for n in range(1, 10):
                    matrix[i][j] = str(n)
                    if isValidSudoku(matrix):
                        if f:
                            f = False
                            cand = -1
                            matrix[i][j] = '.'
                            break
                        else:
                            f = True
                            cand = n

                    matrix[i][j] = '.'
                if f:
                    matrix[i][j] = str(cand)
                    return matrix


class Node:
    def __init__(self, val: Union["Board", str]):
        self.val = val if isinstance(val, Board) else Board(val)

    def __eq__(self, other):
        return self.val == other.val


def dfs(node: Node, verbose=False, max_depth=sys.maxsize):
    stack = [node.val]
    for i in range(int(max_depth)):
        node = stack.pop(-1)

        if node.win():
            return node.tolist()

        stack.extend(node.get_next_step())

        if verbose and i > 0 and i % 1000 == 0:
            print(i, node)

    return None


def isValidSudoku(board: List[List[str]]) -> bool:
    rows = [0, 0, 0, 0, 0, 0, 0, 0, 0]  # 9's 0
    cols = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    boxes = [0, 0, 0, 0, 0, 0, 0, 0, 0]

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


class Board:
    def __init__(self, board: Union[List[List[str]], str]):
        if isinstance(board, str):
            self.board = board
        else:
            self.board = '|'.join([''.join(r) for r in board])

    def __repr__(self):
        return self.board

    def __eq__(self, other):
        return self.board == other.board

    def tolist(self):
        return [list(s) for s in self.board.split('|')]

    def is_valid(self):
        return isValidSudoku(self.tolist())

    def get_next_step(self) -> List["Board"]:
        matrix = self.tolist()

        results = []
        for i in range(9):
            for j in range(9):
                if matrix[i][j] == '.':
                    for cand in range(1, 10):
                        matrix[i][j] = str(cand)
                        flag = isValidSudoku(matrix)

                        if flag:
                            results.append(Board(matrix))
                    matrix[i][j] = '.'
        return results

    def win(self) -> bool:
        return '.' not in self.board and self.is_valid()


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        matrix = board
        board = Board(board)

        flag = True
        while flag:
            temp = put_one(board)
            if temp is None:
                break
            else:
                board = Board(temp)

        if not board.win():
            print('Do DFS!')

        board = dfs(Node(board), verbose=True)

        matrix[:] = board
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

    n_masks = 50
    rng = np.random.default_rng()
    mask = rng.permutation(81)[:n_masks]
    masked = copy.deepcopy(answer)

    for m in mask:
        r, c = divmod(m, 9)
        masked[r][c] = '.'

    # test.addTest(
    #     masked, answer
    # )
    test.addTest(
        game, answer
    )
    test.doTest()

    # print(Board(game))
    # print(Board(put_one(Board(game))))
    # print(solution.solveSudoku(game))
