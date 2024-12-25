package io.petesong.leetcode;

import io.petesong.leetcode.LeetCode33.Solution;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;

import java.util.stream.Stream;

/**
 * LeetCode33 test.
 */
public class LeetCode33Test {
  static Stream<Arguments> intArrayIntIntProvider() {
    return Stream.of(
        // edge cases
        Arguments.arguments(null, 0, -1),
        Arguments.arguments(new int[0], 0, -1),
        Arguments.arguments(new int[5001], -1, -1),
        Arguments.arguments(new int[10], (int) -1e4 - 1, -1),
        Arguments.arguments(new int[10], (int) 1e4 + 1, -1),

        // regular cases
        // found it
        Arguments.arguments(new int[]{4, 5, 6, 7, 0, 1, 2}, 0, 4),
        Arguments.arguments(new int[]{4, 5, 6, 7, 0, 1, 2}, 1, 5),
        Arguments.arguments(new int[]{4, 5, 6, 7, 0, 1, 2}, 2, 6),
        Arguments.arguments(new int[]{4, 5, 6, 7, 0, 1, 2}, 7, 3),
        Arguments.arguments(new int[]{4, 5, 6, 7, 0, 1, 2}, 6, 2),
        Arguments.arguments(new int[]{4, 5, 6, 7, 0, 1, 2}, 5, 1),
        Arguments.arguments(new int[]{4, 5, 6, 7, 0, 1, 2}, 4, 0),
        Arguments.arguments(new int[]{5, 6, 7, 0, 1, 2, 3}, 0, 3),
        Arguments.arguments(new int[]{5, 6, 7, 0, 1, 2, 3}, 1, 4),
        Arguments.arguments(new int[]{5, 6, 7, 0, 1, 2, 3}, 2, 5),
        Arguments.arguments(new int[]{5, 6, 7, 0, 1, 2, 3}, 3, 6),
        Arguments.arguments(new int[]{5, 6, 7, 0, 1, 2, 3}, 7, 2),
        Arguments.arguments(new int[]{5, 6, 7, 0, 1, 2, 3}, 6, 1),
        Arguments.arguments(new int[]{5, 6, 7, 0, 1, 2, 3}, 5, 0),

        // Not found it.
        Arguments.arguments(new int[]{5, 6, 7, 0, 1, 2, 3}, 101, -1)
    );
  }

  @ParameterizedTest
  @MethodSource("intArrayIntIntProvider")
  void search(int[] nums, int target, int expected) {
    int actualResult = new Solution().search(nums, target);
    Assertions.assertEquals(expected, actualResult);
  }

}
