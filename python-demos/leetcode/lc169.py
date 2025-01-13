"""
* 169. Majority Element
* https://leetcode.com/problems/majority-element/description/
"""


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        """
        assume that the majority element always exists in the array
        """
        if nums is None or not isinstance(nums, list) or len(nums) == 0:
            raise ValueError("There must be a majority element in the array.")
        element = 0
        element_count = 0
        for num in nums:
            if element_count == 0:
                element = num
                element_count = 1
            else:
                if num == element:
                    element_count += 1
                else:
                    element_count -= 1
        return element

    def majorityElement2(self, nums: list[int]) -> int:
        if nums is None or not isinstance(nums, list) or len(nums) == 0:
            raise ValueError("There must be a majority element in the array.")
        nums.sort()
        return nums[len(nums) // 2]


def main() -> None:  # pragma: no cover
    nums = [3, 2, 3]
    assert 3 == Solution().majorityElement(nums)


if __name__ == "__main__":
    main()
