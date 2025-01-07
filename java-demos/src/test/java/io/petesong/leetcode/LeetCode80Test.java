package io.petesong.leetcode;

import io.petesong.leetcode.LeetCode80.Solution;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;

import java.util.stream.Stream;

/**
 * LeetCode80 test.
 */
public class LeetCode80Test {
  static Stream<Arguments> intArrayIntProvider() {
    return Stream.of(
        // edge cases
        Arguments.arguments(null, -1),
        Arguments.arguments(new int[]{}, -1),
        Arguments.arguments(new int[]{1}, 1),
        Arguments.arguments(new int[]{1, 1}, 2),

        // regular cases
        Arguments.arguments(new int[]{1, 1, 1, 2, 2, 3}, 5),
        Arguments.arguments(new int[]{0, 0, 1, 1, 1, 1, 2, 3, 3}, 7),
        Arguments.arguments(new int[]{4, 4, 4, 4, 4, 4, 4, 4}, 2)
    );
  }

  @ParameterizedTest
  @MethodSource("intArrayIntProvider")
  void removeDuplicates(int[] nums, int expected) {
    int actualResult = new Solution().removeDuplicates(nums);
    Assertions.assertEquals(expected, actualResult);
  }

}
