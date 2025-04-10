"""
# 36. Valid Sudoku
# https://leetcode.com/problems/valid-sudoku/description/
"""

from collections import defaultdict


class Solution:
    def valid_args(self, board: list[list[str]]) -> bool:
        if board is None or (not isinstance(board, list)) or len(board) != 9:
            return False
        if not all(isinstance(row, list) and len(row) == 9 for row in board):
            return False
        valid_elements = set("123456789.")
        return all(isinstance(elem, str) and elem in valid_elements for row in board for elem in row)

    def isValidSudoku(self, board: list[list[str]]) -> bool:
        if not self.valid_args(board):
            raise ValueError("Invalid board")

        rows: dict[int, set[str]] = defaultdict(set)
        cols: dict[int, set[str]] = defaultdict(set)
        boxes: dict[int, set[str]] = defaultdict(set)
        for i in range(9):
            for j in range(9):
                if (elem := board[i][j]) == ".":
                    continue
                box_index = (i // 3) * 3 + (j // 3)
                if elem in rows[i] or elem in cols[j] or elem in boxes[box_index]:
                    print("2")
                    return False
                rows[i].add(elem)
                cols[j].add(elem)
                boxes[box_index].add(elem)
        return True

    def isValidSudoku2(self, board: list[list[str]]) -> bool:
        if not self.valid_args(board):
            raise ValueError("Invalid board")

        # Check rows
        for row in board:
            filtered_row = [elem for elem in row if elem != "."]
            if len(filtered_row) != len(set(filtered_row)):
                print("2")
                return False

        # Check columns
        for i in range(9):
            seen = set()
            for j in range(9):
                if (elem := board[j][i]) != ".":
                    if elem in seen:
                        print("3")
                        return False
                    seen.add(elem)

        # Check 3*3 sub-boxes
        for box_row in range(3):
            for box_col in range(3):
                seen = set()
                for r in range(3):
                    for c in range(3):
                        if (elem := board[box_row * 3 + r][box_col * 3 + c]) != ".":
                            if elem in seen:
                                print("4")
                                return False
                            seen.add(elem)

        return True


def main() -> None:  # pragma: no cover
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    sol = Solution()
    print(sol.isValidSudoku(board))

    board = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    print(sol.isValidSudoku(board))
    board = [
        [".", ".", "4", ".", ".", ".", "6", "3", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        ["5", ".", ".", ".", ".", ".", ".", "9", "."],
        [".", ".", ".", "5", "6", ".", ".", ".", "."],
        ["4", ".", "3", ".", ".", ".", ".", ".", "1"],
        [".", ".", ".", "7", ".", ".", ".", ".", "."],
        [".", ".", ".", "5", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
    ]
    print(sol.isValidSudoku(board))


if __name__ == "__main__":
    main()
