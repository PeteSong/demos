"""
# 2512. Reward Top K Students
# https://leetcode.com/problems/reward-top-k-students/description/
"""

from collections import defaultdict
from heapq import heappop, heappush, heappushpop


class Solution:
    def valid_arg(
        self,
        positive_feedback: list[str],
        negative_feedback: list[str],
        report: list[str],
        student_id: list[int],
        k: int,
    ) -> bool:
        max_len = 10**4
        for arr in [positive_feedback, negative_feedback, report, student_id]:
            if arr is None or not isinstance(arr, list) or (l1 := len(arr)) == 0 or l1 > max_len:
                return False
        if (l1 := len(student_id)) != len(report) or l1 != len(set(student_id)):
            return False
        for arr in [positive_feedback, negative_feedback, report]:
            if any(elem is None or not isinstance(elem, str) or (l1 := len(elem)) < 1 or l1 > 100 for elem in arr):
                return False
        if any(s_id is None or not isinstance(s_id, int) or s_id < 1 or s_id > 10**9 for s_id in student_id):
            return False
        if k is None or not isinstance(k, int) or k < 1 or k > len(report):
            return False
        return True

    def topStudents(
        self,
        positive_feedback: list[str],
        negative_feedback: list[str],
        report: list[str],
        student_id: list[int],
        k: int,
    ) -> list[int]:
        if not self.valid_arg(positive_feedback, negative_feedback, report, student_id, k):
            raise ValueError("Invalid argument")
        points = []
        positive_feedback_set = set(positive_feedback)
        negative_feedback_set = set(negative_feedback)
        for student_report in report:
            point = 0
            for word in student_report.split():
                if word in positive_feedback_set:
                    point += 3
                elif word in negative_feedback_set:
                    point -= 1
            points.append(point)
        point_students = defaultdict(list)
        for s_id, point in zip(student_id, points):
            point_students[point].append(s_id)

        result = []
        for point in sorted(point_students.keys(), reverse=True):
            if len(result) >= k:
                break
            result.extend(sorted(point_students[point]))
        return result[:k]

    def topStudents2(
        self,
        positive_feedback: list[str],
        negative_feedback: list[str],
        report: list[str],
        student_id: list[int],
        k: int,
    ) -> list[int]:
        if not self.valid_arg(positive_feedback, negative_feedback, report, student_id, k):
            raise ValueError("Invalid argument")
        pfs = set(positive_feedback)
        nfs = set(negative_feedback)
        min_heap = []
        for s_id, s_report in zip(student_id, report):
            point = 0
            for word in s_report.split():
                if word in pfs:
                    point += 3
                elif word in nfs:
                    point -= 1
            item = point, -s_id
            if len(min_heap) < k:
                heappush(min_heap, item)
            else:
                heappushpop(min_heap, item)
        top_ids = []
        for _ in range(k):
            top_ids.append(-(heappop(min_heap)[1]))
        # do not use list comprehension, should use `heappop`
        # top_ids = [-s_id for _, s_id in min_heap]
        return top_ids[::-1]


def main() -> None:  # pragma: no cover
    positive_feedback = ["smart", "brilliant", "studious"]
    negative_feedback = ["not"]
    report = ["this student is not studious", "the student is smart"]
    student_id = [1, 2]
    k = 2
    solution = Solution()
    print(solution.topStudents(positive_feedback, negative_feedback, report, student_id, k))
    print(solution.topStudents2(positive_feedback, negative_feedback, report, student_id, k))

    print()

    report = ["this student is studious", "the student is smart"]
    print(solution.topStudents(positive_feedback, negative_feedback, report, student_id, k))
    print(solution.topStudents2(positive_feedback, negative_feedback, report, student_id, k))


if __name__ == "__main__":
    main()
