import pytest

from leetcode.lc36 import Solution


class TestSolution:
    test_invalid_data = [
        (None),
        ("SSS"),
        ([]),
        ([1]),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9]),
        ([[1, 2, 3, 4, 5, 6, 7, 8]]),
        (
            [
                ["5", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", 9, "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", "-", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"],
            ]
        ),
    ]

    test_data = [
        (
            True,
            [
                ["5", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"],
            ],
        ),
        (
            False,
            [
                ["5", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", "8", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"],
            ],
        ),
        (
            False,
            [
                ["8", "3", ".", ".", "7", ".", "7", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"],
            ],
        ),
        (
            False,
            [
                [".", ".", "4", ".", ".", ".", "6", "3", "."],
                [".", "5", ".", ".", ".", ".", ".", ".", "."],
                ["5", ".", ".", ".", ".", ".", ".", "9", "."],
                [".", ".", ".", "5", "6", ".", ".", ".", "."],
                ["4", ".", "3", ".", ".", ".", ".", ".", "1"],
                [".", ".", ".", "7", ".", ".", ".", ".", "."],
                [".", ".", ".", "5", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", ".", "."],
            ],
        ),
    ]

    @pytest.mark.parametrize("board", test_invalid_data)
    def test_invalid_data(self, board):
        with pytest.raises(ValueError):
            Solution().isValidSudoku(board)
        with pytest.raises(ValueError):
            Solution().isValidSudoku2(board)

    @pytest.mark.parametrize("expected, board", test_data)
    def test_isValidSudoku(self, expected, board):
        assert Solution().isValidSudoku(board) == expected
        assert Solution().isValidSudoku2(board) == expected
