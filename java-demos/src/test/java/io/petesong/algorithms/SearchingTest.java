package io.petesong.algorithms;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;

import java.util.stream.Stream;

/**
 * Searching test.
 */
public class SearchingTest {
  static Stream<Arguments> intArrayIntProvider() {
    return Stream.of(
        // edge cases
        Arguments.arguments(null, 0, -1),
        Arguments.arguments(new int[0], 0, -1),
        Arguments.arguments(new int[8], 9, -1),

        // regular cases
        Arguments.arguments(new int[]{1, 3, 5, 7, 9, 10, 14}, 1, 0),
        Arguments.arguments(new int[]{1, 3, 5, 7, 9, 10, 14}, 3, 1),
        Arguments.arguments(new int[]{1, 3, 5, 7, 9, 10, 14}, 5, 2),
        Arguments.arguments(new int[]{1, 3, 5, 7, 9, 10, 14}, 7, 3),
        Arguments.arguments(new int[]{1, 3, 5, 7, 9, 10, 14}, 9, 4),
        Arguments.arguments(new int[]{1, 3, 5, 7, 9, 10, 14}, 10, 5),
        Arguments.arguments(new int[]{1, 3, 5, 7, 9, 10, 14}, 14, 6)
    );
  }

  @ParameterizedTest
  @MethodSource("intArrayIntProvider")
  void binarySearch(int[] a, int key, int expected) {
    int actualResult = Searching.binarySearch(a, key);
    Assertions.assertEquals(expected, actualResult);
  }
}
