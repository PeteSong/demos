import pytest

from leetcode.lc692 import Solution


class TestSolution:
    list_0_100001 = list(range(10**5 + 1))
    invalid_test_data = [
        (None, None),
        ("SSS", None),
        ([], None),
        (list_0_100001, None),
        ([1, 1, 2, 2, 3], None),
        ([1, 1, 2, 2, 3], "SSS"),
        ([1, 1, 2, 2, 3], 0),
        ([1, 1, 2, 2, 3], 5),
        ([1, "1", "2", 2, 3], 2),
        (["", "a", "b", "c", "a", "b"], 2),
        (["a" * 11, "b", "c", "b"], 2),
    ]
    valid_test_data = [
        (["i", "love"], ["i", "love", "leetcode", "i", "love", "coding"], 2),
        (["i", "love", "coding"], ["i", "love", "leetcode", "i", "love", "coding"], 3),
        (["the"], ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 1),
        (["the", "is"], ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 2),
        (["the", "is", "sunny"], ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 3),
    ]

    @pytest.mark.parametrize("words, k", invalid_test_data)
    def test_invalid_input(self, words, k):
        with pytest.raises(ValueError):
            Solution().topKFrequent(words, k)

    @pytest.mark.parametrize("expected, words, k", valid_test_data)
    def test_topKFrequent(self, expected, words, k):
        assert sorted(Solution().topKFrequent(words, k)) == sorted(expected)
