from leetcode_tester import Tester

from typing import Optional, List


class Solution:
    # # Approach 1: Divide matrix into 4 parts
    # def rotate(self, matrix: List[List[int]]) -> None:
    #     """
    #     Do not return anything, modify matrix in-place instead.
    #     """
    #     n = len(matrix)
    #     a = (n + 1) // 2
    #     b = n - a
    #     mid = (n - 1) / 2
    #
    #     for i in range(a):
    #         for j in range(b):
    #             dr = mid - i
    #             dc = mid - j
    #
    #             idx = [
    #                 [int(mid - dr), int(mid - dc)],
    #                 [int(mid - dc), int(mid + dr)],
    #                 [int(mid + dr), int(mid + dc)],
    #                 [int(mid + dc), int(mid - dr)]
    #             ]
    #
    #             temp = [matrix[r][c] for r, c in idx]
    #
    #             for k, (r, c) in enumerate(idx):
    #                 matrix[r][c] = temp[k - 1]
    #
    #     return matrix

    # # Approach 1 better implementation
    # def rotate(self, matrix: List[List[int]]) -> None:
    #     n = len(matrix)
    #
    #     for i in range(n // 2 + n % 2):
    #         for j in range(n // 2):
    #             tmp = matrix[n - 1 - j][i]
    #             matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
    #             matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 - i]
    #             matrix[j][n - 1 - i] = matrix[i][j]
    #             matrix[i][j] = tmp
    #
    #     return matrix

    # Approach 2: Transpose than reflect via y axis
    def rotate(self, matrix: List[List[int]]) -> None:
        self.transpose(matrix)
        self.reflect(matrix)

        return matrix

    def transpose(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    def reflect(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][n - j - 1] = \
                    matrix[i][n - j - 1], matrix[i][j]


if __name__ == '__main__':
    solution = Solution()
    test = Tester(solution.rotate)

    test.addTest(
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    )
    test.addTest(
        [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]],
        [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
    )
    test.doTest()

    # print(solution.rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
