# 1480. Running Sum of 1d Array
# https://leetcode.com/problems/running-sum-of-1d-array/description/


class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        running_sum = [0]
        for n in nums:
            t = running_sum[-1] + n
            running_sum.append(t)
        del running_sum[0]
        return running_sum


def main():
    nums = [1, 2, 3, 4]
    expected_result = [1, 3, 6, 10]
    r = Solution().runningSum(nums) == expected_result
    print(f"Is passed: {r}")
    assert r


if __name__ == "__main__":
    main()
