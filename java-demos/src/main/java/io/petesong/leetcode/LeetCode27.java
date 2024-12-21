package io.petesong.leetcode;

import java.util.Objects;

/**
 * 27. Remove Element.
 * https://leetcode.com/problems/remove-element/description/
 */
class LeetCode27 {

  static class Solution {
    boolean validArgs(int[] nums, int val) {
      if (Objects.isNull(nums) || nums.length == 0 || nums.length > 100) {
        return false;
      }
      if (val < 0 || val > 100) {
        return false;
      }
      return true;
    }

    public int removeElement(int[] nums, int val) {
      if (!validArgs(nums, val)) {
        return 0;
      }
      int p1 = 0;
      int p2 = nums.length - 1;
      while (p1 <= p2) {
        if (nums[p1] == val) {
          int tmp = nums[p1];
          nums[p1] = nums[p2];
          nums[p2] = tmp;
          p2--;
        } else {
          p1++;
        }
      }
      return p1;
    }

  }

  // use the annotation below to 'no cover'
  @lombok.Generated
  public static void main(String[] args) {
    int[] nums = {3, 2, 2, 3};
    int val = 2;
    int expectedResult = 2;
    int actualResult = new LeetCode27.Solution().removeElement(nums, val);
    boolean isPassed = expectedResult == actualResult;
    System.out.printf("Is passed: %b", isPassed);
    assert isPassed;
  }
}
