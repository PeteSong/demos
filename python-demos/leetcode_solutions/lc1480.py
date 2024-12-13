# 1480. Running Sum of 1d Array
# https://leetcode.com/problems/running-sum-of-1d-array/description/


class Solution:
    def valid_arg(self, nums: list[int]) -> bool:
        if nums is None or (not isinstance(nums, list)) or len(nums) == 0:
            return False
        return True

    def runningSum(self, nums: list[int]) -> list[int]:
        if not self.valid_arg(nums):
            return []
        running_sum = [0]
        for n in nums:
            t = running_sum[-1] + n
            running_sum.append(t)
        del running_sum[0]
        return running_sum

    def runningSum2(self, nums: list[int]) -> list[int]:
        if not self.valid_arg(nums):
            return []
        running_sum = [nums[0]]
        for n in nums[1:]:
            t = running_sum[-1] + n
            running_sum.append(t)
        return running_sum


def main() -> None:  # pragma: no cover
    nums = [1, 2, 3, 4]
    expected_result = [1, 3, 6, 10]
    r = Solution().runningSum(nums) == expected_result
    print(f"Is passed: {r}")
    assert r
    r = Solution().runningSum2(nums) == expected_result
    print(f"Is passed: {r}")
    assert r


if __name__ == "__main__":
    main()
