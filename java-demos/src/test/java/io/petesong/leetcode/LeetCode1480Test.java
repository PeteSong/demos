package io.petesong.leetcode;

import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;

import java.util.stream.Stream;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;

import io.petesong.leetcode.LeetCode1480.Solution;

/**
 * LeetCode13 test.
 */
public class LeetCode1480Test {
  static Stream<Arguments> intIntProvider() {
    return Stream.of(
        Arguments.arguments(null, new int[0]),
        Arguments.arguments(new int[0], new int[0]),
        Arguments.arguments(new int[]{1}, new int[]{1}),
        Arguments.arguments(new int[]{1, 2}, new int[]{1, 3}),
        Arguments.arguments(new int[]{1, 2, 3, 4}, new int[]{1, 3, 6, 10})
    );
  }

  @ParameterizedTest
  @MethodSource("intIntProvider")
  void fizzBuzz(int[] nums, int[] expected) {
    int[] actualResult = new Solution().runningSum(nums);
    assertArrayEquals(expected, actualResult);
  }

}
