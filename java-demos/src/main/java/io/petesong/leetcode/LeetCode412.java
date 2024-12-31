package io.petesong.leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * 412. Fizz Buzz
 * https://leetcode.com/problems/fizz-buzz/
 */
class LeetCode412 {
  static final String FIZZ = "Fizz";
  static final String BUZZ = "Buzz";
  static final String FIZZBUZZ = FIZZ + BUZZ;
  static final int FIVE = 5;
  static final int THREE = 3;

  static class Solution {
    public List<String> fizzBuzz(int n) {
      List<String> ans = new ArrayList<>();
      int i = 1;
      while (i <= n) {
        String s = "";
        if (i % THREE == 0 && i % FIVE == 0) {
          ans.add(FIZZBUZZ);
        } else if (i % THREE == 0) {
          ans.add(FIZZ);
        } else if (i % FIVE == 0) {
          ans.add(BUZZ);
        } else {
          ans.add(String.valueOf(i));
        }
        i++;
      }
      return ans;
    }
  }

  // use the annotation below to 'no cover'
  @lombok.Generated
  public static void main(String[] args) {
    int n = 15;
    String[] expectedR = {"1", "2", FIZZ, "4", BUZZ,
        FIZZ, "7", "8", FIZZ, BUZZ,
        "11", FIZZ, "13", "14", FIZZBUZZ};
    List<String> expectedResult = Arrays.asList(expectedR);
    List<String> actualResult = new LeetCode412.Solution().fizzBuzz(n);
    boolean isPassed = expectedResult.equals(actualResult);
    System.out.printf("Is passed: %b", isPassed);
    assert isPassed;
  }
}
