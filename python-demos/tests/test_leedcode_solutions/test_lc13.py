from leetcode_solutions.lc13 import Solution


class TestSolution:
    def test_romanToInt(self):
        s = "MCMXCIV"
        expected_result = 1994
        assert Solution().romanToInt(s) == expected_result

    def test_romanToInt2(self):
        s = "MCMXCIV"
        expected_result = 1994
        assert Solution().romanToInt2(s) == expected_result
