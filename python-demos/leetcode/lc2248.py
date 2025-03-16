"""
# 2248. Intersection of Multiple Arrays
# https://leetcode.com/problems/intersection-of-multiple-arrays/description/
"""


class Solution:
    def valid_arg(self, nums: list[list[int]]) -> bool:
        if nums is None or not isinstance(nums, list) or (l1 := len(nums)) == 0 or l1 > 1000:
            return False
        if any(not isinstance(numa, list) for numa in nums):
            return False
        lens = list(map(len, nums))
        lens_set = list(map(len, (map(set, nums))))
        if lens != lens_set:
            return False
        total_len = sum(lens)
        if total_len > 1000:
            return False
        if any((not isinstance(n, int)) or (n < 1) or (n > 1000) for numa in nums for n in numa):
            return False
        return True

    def intersection(self, nums: list[list[int]]) -> list[int]:
        if not self.valid_arg(nums):
            return []
        nums_len = len(nums)
        t = {}
        # flatten_nums = [n for numa in nums for n in numa]
        # for n in flatten_nums:
        #     t[n] = t.get(n, 0) + 1
        for numa in nums:
            for n in numa:
                t[n] = t.get(n, 0) + 1
        res = [k for k, v in t.items() if v == nums_len]
        res.sort()
        return res

    def intersection2(self, nums: list[list[int]]) -> list[int]:
        if not self.valid_arg(nums):
            return []
        return sorted(set.intersection(*map(set, nums)))

    def intersection3(self, nums: list[list[int]]) -> list[int]:
        if not self.valid_arg(nums):
            return []
        res = set(nums[0])
        res.intersection_update(*nums[1:])
        return sorted(res)

    def intersection4(self, nums: list[list[int]]) -> list[int]:
        if not self.valid_arg(nums):
            return []
        t1 = {}
        for n in nums[0]:
            t1[n] = t1.get(n, 0) + 1
        res = []
        for k in t1:
            if all(k in numa for numa in nums[1:]):
                res.append(k)
        return sorted(res)


def main() -> None:  # pragma: no cover
    nums = [[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]]
    s = Solution()
    print(s.intersection(nums))
    print(s.intersection2(nums))
    print(s.intersection3(nums))
    print(s.intersection4(nums))


if __name__ == "__main__":
    main()
