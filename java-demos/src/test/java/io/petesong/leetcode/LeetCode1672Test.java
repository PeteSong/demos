package io.petesong.leetcode;

import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;

import java.util.stream.Stream;

import static org.junit.jupiter.api.Assertions.assertEquals;

import io.petesong.leetcode.LeetCode1672.Solution;

/**
 * LeetCode13 test.
 */
public class LeetCode1672Test {
  static Stream<Arguments> intIntProvider() {
    return Stream.of(
        Arguments.arguments(null, 0),
        Arguments.arguments(new int[][]{{}}, 0),
        Arguments.arguments(new int[][]{{9}}, 9),
        Arguments.arguments(new int[][]{{9, 5}, {1, 9}}, 14)
    );
  }

  @ParameterizedTest
  @MethodSource("intIntProvider")
  void fizzBuzz(int[][] accounts, int expected) {
    int actualResult = new Solution().maximumWealth(accounts);
    assertEquals(expected, actualResult);
  }

}
