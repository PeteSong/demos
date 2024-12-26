import pytest

from leetcode_solutions.lc79 import Solution


class TestSolution:
    test_data = [
        # edge cases
        (None, "", False),
        ("string", 0, False),
        ([], 0, False),
        ([1], 1.5, False),
        ([[]], "", False),
        ([[], [], [], [], [], [], []], "", False),
        ([[0, 1, 2, 3, 4, 5, 6], [], [], [], [], []], "", False),
        ([[0, 1, 2, 3, 4, 5], [], [], [], [], []], None, False),
        ([[0, 1, 2, 3, 4, 5], [], [], [], [], []], 3, False),
        ([[0, 1, 2, 3, 4, 5], [], [], [], [], []], "", False),
        ([[0, 1, 2, 3, 4, 5], [], [], [], [], []], "abcdefghijklmnopqrstuvwxyz", False),
        ([[0, 1, 2], [0, 1, 2], [0, 1, 2]], "abcdefghij", False),
        # regular cases
        ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED", True),
        ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE", True),
        ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB", False),
        ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCX", False),
    ]

    @pytest.mark.parametrize("board,word,expected", test_data)
    def test_exist(self, board, word, expected):
        assert Solution().exist(board, word) == expected
