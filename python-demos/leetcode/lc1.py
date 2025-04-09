"""
# 1. Two Sum
# https://leetcode.com/problems/two-sum/description/
"""


class Solution:
    edge_num = 10**9

    def valid_args(self, nums: list[int], target: int) -> bool:
        if nums is None or (not isinstance(nums, list)) or (nums_len := len(nums)) < 2 or nums_len > 10**4:
            return False
        if target is None or not isinstance(target, int) or not (-self.edge_num <= target <= self.edge_num):
            return False
        return all(isinstance(n, int) and -self.edge_num <= n <= self.edge_num for n in nums)

    def twoSum(self, nums: list[int], target: int) -> list[int] | None:
        if not self.valid_args(nums, target):
            return None

        m: dict[int, int] = {}
        for i, v in enumerate(nums):
            diff = target - v
            if diff in m:
                return [m[diff], i]
            m[v] = i

    def twoSum2(self, nums: list[int], target: int) -> list[int] | None:
        if not self.valid_args(nums, target):
            return None

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


def main() -> None:  # pragma: no cover
    inputs = (([2, 7, 11, 15], 9), ([3, 2, 4], 6), ([3, 3], 6))
    solution = Solution()
    for nums, target in inputs:
        result = solution.twoSum(nums, target)
        print(result)
        result = solution.twoSum2(nums, target)
        print(result)
        print()


if __name__ == "__main__":
    main()
