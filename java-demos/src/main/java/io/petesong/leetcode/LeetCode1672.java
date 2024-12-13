package io.petesong.leetcode;

/**
 * 1672. Richest Customer Wealth
 * https://leetcode.com/problems/richest-customer-wealth/description/
 */
class LeetCode1672 {
  static class Solution {
    public int maximumWealth(int[][] accounts) {
      int maxAmt = 0;
      for (int i = 0; i < accounts.length; i++) {
        int t = 0;
        for (int n : accounts[i]) {
          t += n;
        }
        if (t > maxAmt) {
          maxAmt = t;
        }
      }
      return maxAmt;
    }
  }

  public static void main(String[] args) {
    int[][] accounts = {{1, 5}, {7, 3}, {3, 5}};
    int expectedResult = 10;
    int actualResult = new LeetCode1672.Solution().maximumWealth(accounts);
    boolean isPassed = expectedResult == actualResult;
    System.out.printf("Is passed: %b", isPassed);
    assert isPassed;
  }
}
