package io.petesong.leetcode;

import java.util.Arrays;

/**
 * 1480. Running Sum of 1d Array
 * https://leetcode.com/problems/running-sum-of-1d-array/description/
 */
class LeetCode1480 {
  static class Solution {
    public int[] runningSum(int[] nums) {
      int[] runningS = Arrays.copyOf(nums, nums.length);
      for (int i = 1; i < nums.length; i++) {
        runningS[i] = runningS[i] + runningS[i - 1];
      }
      return runningS;
    }
  }

  public static void main(String[] args) {
    int[] nums = {1, 2, 3, 4};
    int[] expectedResult = {1, 3, 6, 10};
    int[] actualResult = new LeetCode1480.Solution().runningSum(nums);
    boolean isPassed = Arrays.equals(expectedResult, actualResult);
    System.out.printf("Is passed: %b", isPassed);
    assert isPassed;
  }
}
