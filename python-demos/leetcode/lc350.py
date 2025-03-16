"""
# 350. Intersection of Two Arrays II
# https://leetcode.com/problems/intersection-of-two-arrays-ii/description/
"""


class Solution:
    def valid_arg(self, nums1: list[int], nums2: list[int]) -> bool:
        if (nums1 is None or (l1 := len(nums1)) == 0) or (nums2 is None or (l2 := len(nums2)) == 0):
            return False
        if l1 > 1000 or l2 > 1000:
            return False
        if any((not isinstance(n, int)) or (n < 1) or (n > 1000) for n in nums1):
            return False
        if any((not isinstance(n, int)) or (n < 1) or (n > 1000) for n in nums2):
            return False
        return True

    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        if not self.valid_arg(nums1, nums2):
            return []
        t1 = {}
        for n in nums1:
            t1[n] = t1.get(n, 0) + 1
        res = []
        for n in nums2:
            if t1.get(n, 0) > 0:
                res.append(n)
                t1[n] -= 1
        return res


def main() -> None:  # pragma: no cover
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    s = Solution()
    print(s.intersection(nums1, nums2))


if __name__ == "__main__":
    main()
