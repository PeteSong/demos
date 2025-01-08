"""
# 79. Word Search
# https://leetcode.com/problems/word-search/description/
"""

import collections
import itertools


class Solution:
    def valid_args(self, board: list[list[str]], word: str) -> bool:
        if (
            board is None
            or (not isinstance(board, list))
            or (m := len(board)) == 0
            or (not isinstance(board[0], list))
            or (n := len(board[0])) == 0
        ):
            return False
        if m > 6 or n > 6:
            return False
        if word is None or (not isinstance(word, str)) or (word_len := len(word)) == 0:
            return False
        if word_len > 15 or word_len > m * n:
            return False
        return True

    def exist(self, board: list[list[str]], word: str) -> bool:
        def dfs(m: int, n: int, index: int) -> bool:
            if index == len(word):
                return True
            if m < 0 or m >= row_count or n < 0 or n >= col_count or board[m][n] != word[index]:
                return False
            # print(m, n, index, word[index])
            temp, board[m][n] = board[m][n], "#"
            adjacent_cells = [
                (m + 1, n),
                (m - 1, n),
                (m, n + 1),
                (m, n - 1),
            ]
            found = any([dfs(*cell, index + 1) for cell in adjacent_cells])
            board[m][n] = temp
            return found

        if not self.valid_args(board, word):
            return False

        row_count, col_count = len(board), len(board[0])
        counter = collections.Counter(itertools.chain(*board))
        # if letters in word but not in board
        if not set(word) <= set(counter.keys()):
            return False
        # if the first letter in word is more in board than the final letter in word
        if counter[word[0]] > counter[word[-1]]:
            word = word[::-1]

        for row in range(row_count):
            for col in range(col_count):
                if board[row][col] != word[0]:
                    continue
                if dfs(row, col, 0):
                    return True

        return False


def main() -> None:  # pragma: no cover
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    result = Solution().exist(board, word)
    print(f"Existing: {result}")


if __name__ == "__main__":
    main()
