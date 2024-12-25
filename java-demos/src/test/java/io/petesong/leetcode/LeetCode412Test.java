package io.petesong.leetcode;

import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Stream;

import static org.junit.jupiter.api.Assertions.assertEquals;

import io.petesong.leetcode.LeetCode412.Solution;

/**
 * LeetCode412 test.
 */
public class LeetCode412Test {
  static Stream<Arguments> intListProvider() {
    return Stream.of(
        Arguments.arguments(-10, Arrays.asList()),
        Arguments.arguments(0, Arrays.asList()),
        Arguments.arguments(1, Arrays.asList("1")),
        Arguments.arguments(3, Arrays.asList("1", "2", LeetCode412.FIZZ)),
        Arguments.arguments(15,
            Arrays.asList("1", "2", LeetCode412.FIZZ, "4", LeetCode412.BUZZ,
                LeetCode412.FIZZ, "7", "8", LeetCode412.FIZZ, LeetCode412.BUZZ,
                "11", LeetCode412.FIZZ, "13", "14", LeetCode412.FIZZBUZZ
            )
        )
    );
  }

  @ParameterizedTest
  @MethodSource("intListProvider")
  void fizzBuzz(int n, List<String> expected) {
    List<String> actualResult = new Solution().fizzBuzz(n);
    assertEquals(expected, actualResult);
  }

}
