package io.petesong.leetcode;

/**
 * 2235. Add Two Integers
 * https://leetcode.com/problems/add-two-integers/
 */
class LeetCode2235 {
  static class Solution {
    public int sum(int num1, int num2) {
      return num1 + num2;
    }
  }

  public static void main(String[] args) {
    int num1 = 3;
    int num2 = 7;
    int expectedResult = 10;
    int actualResult = new LeetCode2235.Solution().sum(num1, num2);
    boolean isPassed = expectedResult == actualResult;
    System.out.printf("Is passed: %b", isPassed);
    assert isPassed;
  }
}

