"""
# 349. Intersection of Two Arrays
# https://leetcode.com/problems/intersection-of-two-arrays/description/
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
        s1 = frozenset(nums1)
        s2 = frozenset(nums2)
        return list(s1 & s2)

    def intersection2(self, nums1: list[int], nums2: list[int]) -> list[int]:
        if not self.valid_arg(nums1, nums2):
            return []
        res = []
        for n in nums1:
            if n in nums2 and n not in res:
                res.append(n)
        return res


def main() -> None:  # pragma: no cover
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    s = Solution()
    print(s.intersection(nums1, nums2))
    print(s.intersection2(nums1, nums2))


if __name__ == "__main__":
    main()
