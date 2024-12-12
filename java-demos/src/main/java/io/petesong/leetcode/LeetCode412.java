package io.petesong.leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * 412. Fizz Buzz
 * https://leetcode.com/problems/fizz-buzz/
 */
class LeetCode412 {
  static final String FIZZBUZZ = "FizzBuzz";
  static final String FIZZ = "Fizz";
  static final String BUZZ = "Buzz";

  static class Solution {
    public List<String> fizzBuzz(int n) {
      List<String> ans = new ArrayList<>();
      int i = 1;
      while (i <= n) {
        if (i % 3 == 0 && i % 5 == 0) {
          ans.add(FIZZBUZZ);
        } else if (i % 3 == 0) {
          ans.add(FIZZ);
        } else if (i % 5 == 0) {
          ans.add(BUZZ);
        } else {
          ans.add(String.valueOf(i));
        }
        i++;
      }
      return ans;
    }
  }

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

