package io.petesong.leetcode;

import io.petesong.leetcode.LeetCode79.Solution;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;

import java.util.stream.Stream;

/**
 * LeetCode33 test.
 */
public class LeetCode79Test {
  static Stream<Arguments> charArrayStringBooleanProvider() {
    return Stream.of(
        // edge cases
        Arguments.arguments(null, "", false),
        Arguments.arguments(new char[][]{}, "", false),
        Arguments.arguments(new char[][]{null}, "", false),
        Arguments.arguments(new char[][]{{}}, "", false),
        Arguments.arguments(new char[][]{{}, {}, {}, {}, {}, {}, {}}, "", false),
        Arguments.arguments(new char[][]{{'a', 'a', 'a', 'a', 'a', 'a', 'a'}, {}, {}, {}, {}, {}, {}}, "", false),
        Arguments.arguments(new char[][]{{'a', 'a', 'a'}, {}, {}}, null, false),
        Arguments.arguments(new char[][]{{'a', 'a', 'a'}, {}, {}}, " ", false),
        Arguments.arguments(new char[][]{{'a', 'a', 'a'}, {}, {}}, "", false),
        Arguments.arguments(new char[][]{{'a', 'a', 'a'}, {}, {}}, "abcdefghijklmno", false),
        Arguments.arguments(new char[][]{{'a', 'a', 'a'}, {}, {}}, "abcdefghij", false),

        // regular cases
        Arguments.arguments(
            new char[][]{{'A', 'B', 'C', 'E'}, {'S', 'F', 'C', 'S'}, {'A', 'D', 'E', 'E'}},
            "ABCCED",
            true
        ),
        Arguments.arguments(
            new char[][]{{'A', 'B', 'C', 'E'}, {'S', 'F', 'C', 'S'}, {'A', 'D', 'E', 'E'}},
            "SEE",
            true
        ),
        // Not found it.
        Arguments.arguments(
            new char[][]{{'A', 'B', 'C', 'E'}, {'S', 'F', 'C', 'S'}, {'A', 'D', 'E', 'E'}},
            "ABCB",
            false
        ),
        Arguments.arguments(
            new char[][]{{'A', 'B', 'C', 'E'}, {'S', 'F', 'C', 'S'}, {'A', 'D', 'E', 'E'}},
            "ABCZ",
            false
        )

    );
  }

  @ParameterizedTest
  @MethodSource("charArrayStringBooleanProvider")
  void exist(char[][] board, String word, boolean expected) {
    boolean actualResult = new Solution().exist(board, word);
    Assertions.assertEquals(expected, actualResult);
  }

}
