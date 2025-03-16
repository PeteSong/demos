import pytest

from leetcode.lc169 import Solution


class TestSolution:
    test_data_edge = [(None), ([]), ("abc")]
    test_data = [
        # regular cases
        (3, [3, 2, 3]),
        (2, [2, 2, 1, 1, 1, 2, 2]),
    ]

    @pytest.mark.parametrize("nums", test_data_edge)
    def test_should_raise_value_error(self, nums):
        with pytest.raises(ValueError):
            Solution().majorityElement(nums)
        with pytest.raises(ValueError):
            Solution().majorityElement2(nums)

    @pytest.mark.parametrize("expected, nums", test_data)
    def test_majorityElement(self, expected, nums):
        assert expected == Solution().majorityElement(nums)
        assert expected == Solution().majorityElement2(nums)
