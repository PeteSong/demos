package io.petesong.leetcode;

import java.util.Objects;

/**
 * 80. Remove Duplicates from Sorted Array II
 * https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/
 */
class LeetCode80 {

  static class Solution {
    private static final int ALLOWED_DUPLICATE_COUNT = 2;

    boolean validArgs(int[] nums) {
      if (Objects.isNull(nums) || nums.length == 0) {
        return false;
      }
      return true;
    }

    public int removeDuplicates(int[] nums) {
      if (!validArgs(nums)) {
        return -1;
      }
      if (nums.length <= ALLOWED_DUPLICATE_COUNT) {
        return nums.length;
      }
      int p = 0;
      for (int i = 0; i < nums.length; i++) {
        if (p < 2 || nums[p - 2] != nums[i]) {
          nums[p] = nums[i];
          p++;
        }
      }
      return p;
    }

  }

  // use the annotation below to 'no cover'
  @lombok.Generated
  public static void main(String[] args) {
    var nums = new int[]{1, 1, 1, 2, 2, 3};
    boolean isPassed = new LeetCode80.Solution().removeDuplicates(nums) == 5;
    System.out.printf("Is passed: %b", isPassed);
    assert isPassed;
  }
}
