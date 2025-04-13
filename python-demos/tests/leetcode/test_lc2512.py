import pytest

from leetcode.lc2512 import Solution


class TestSolution:
    list_0_10001 = list(range(10**4 + 1))
    invalid_test_data = [
        (None, None, None, None, None),
        ("SSS", "SSS", "SSS", "SSS", "SSS"),
        ("SSS", "SSS", "SSS", "SSS", "SSS"),
        ([], [], [], [], []),
        (list_0_10001, list_0_10001, list_0_10001, list_0_10001, list_0_10001),
        ([1, 2], [3], [1, 2], [1], 2),
        ([1, 2], [3], [1, 2], [1, 1], 2),
        ([None], [None], [None], [1, 1], 2),
        (["", "brilliant", "studious"], [""], ["", "the student is smart"], [1, 1], 2),
        (["a" * 101, "brilliant", "studious"], ["b" * 101], ["c" * 101, "the student is smart"], [1, 1], 2),
        (
            ["smart", "brilliant", "studious"],
            ["not"],
            ["this student is studious", "the student is smart"],
            [None, None],
            2,
        ),
        (
            ["smart", "brilliant", "studious"],
            ["not"],
            ["this student is studious", "the student is smart"],
            ["1", "2"],
            2,
        ),
        (["smart", "brilliant", "studious"], ["not"], ["this student is studious", "the student is smart"], [0, 2], 2),
        (
            ["smart", "brilliant", "studious"],
            ["not"],
            ["this student is studious", "the student is smart"],
            [1, 10**9 + 1],
            2,
        ),
        (
            ["smart", "brilliant", "studious"],
            ["not"],
            ["this student is studious", "the student is smart"],
            [1, 2],
            None,
        ),
        (
            ["smart", "brilliant", "studious"],
            ["not"],
            ["this student is studious", "the student is smart"],
            [1, 2],
            "2",
        ),
        (["smart", "brilliant", "studious"], ["not"], ["this student is studious", "the student is smart"], [1, 2], 0),
        (["smart", "brilliant", "studious"], ["not"], ["this student is studious", "the student is smart"], [1, 2], 3),
    ]
    valid_test_data = [
        (
            [1, 2],
            ["smart", "brilliant", "studious"],
            ["not"],
            ["this student is studious", "the student is smart"],
            [1, 2],
            2,
        ),
        (
            [2, 1],
            ["smart", "brilliant", "studious"],
            ["not"],
            ["this student is not studious", "the student is smart"],
            [1, 2],
            2,
        ),
    ]

    @pytest.mark.parametrize("positive_feedback, negative_feedback, report, student_id, k", invalid_test_data)
    def test_invalid_input(self, positive_feedback, negative_feedback, report, student_id, k):
        with pytest.raises(ValueError):
            Solution().topStudents(positive_feedback, negative_feedback, report, student_id, k)
        with pytest.raises(ValueError):
            Solution().topStudents2(positive_feedback, negative_feedback, report, student_id, k)

    @pytest.mark.parametrize("expected, positive_feedback, negative_feedback, report, student_id, k", valid_test_data)
    def test_topStudents(self, expected, positive_feedback, negative_feedback, report, student_id, k):
        solution = Solution()
        assert solution.topStudents(positive_feedback, negative_feedback, report, student_id, k) == expected
        assert solution.topStudents2(positive_feedback, negative_feedback, report, student_id, k) == expected
