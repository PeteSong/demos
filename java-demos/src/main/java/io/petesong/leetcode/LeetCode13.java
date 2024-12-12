package io.petesong.leetcode;

import java.util.Map;

/**
 * 412. Fizz Buzz
 * https://leetcode.com/problems/fizz-buzz/
 */
class LeetCode13 {
  static final Map<String, Integer> ROMAN_INT_MAPPING = Map.ofEntries(
      Map.entry("I", 1),
      Map.entry("IV", 4),
      Map.entry("V", 5),
      Map.entry("IX", 9),
      Map.entry("X", 10),
      Map.entry("XL", 40),
      Map.entry("L", 50),
      Map.entry("XC", 90),
      Map.entry("C", 100),
      Map.entry("CD", 400),
      Map.entry("D", 500),
      Map.entry("CM", 900),
      Map.entry("M", 1000)
  );
  static final int TWO = 2;
  static final int ONE = 1;

  static class Solution {
    public int romanToInt(String s) {
      int n = 0;
      int right = s.length();
      while (right > 0) {
        int w = ONE;
        if (right >= TWO) {
          w = TWO;
        }
        String k = s.substring(right - w, right);
        n += ROMAN_INT_MAPPING.get(k);
        right -= w;
      }
      return n;
    }
  }

  public static void main(String[] args) {
    String s = "MCMXCIV";
    int expectedResult = 1994;
    int actualResult = new LeetCode13.Solution().romanToInt(s);
    boolean isPassed = expectedResult == actualResult;
    System.out.printf("Is passed: %b", isPassed);
    assert isPassed;
  }
}

