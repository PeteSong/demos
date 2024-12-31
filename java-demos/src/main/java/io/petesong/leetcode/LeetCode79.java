package io.petesong.leetcode;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Objects;
import java.util.stream.Collectors;

/**
 * 79. Word Search.
 * https://leetcode.com/problems/word-search/description/
 */
class LeetCode79 {

  static class Solution {
    private char[][] board;
    private String word;
    private int boardRows;
    private int boardCols;

    boolean validArgs() {
      if (Objects.isNull(board) || board.length == 0 || Objects.isNull(board[0])) {
        return false;
      }
      boardRows = board.length;
      boardCols = board[0].length;
      if (boardRows == 0 || boardCols == 0
          || boardRows > 6 || boardCols > 6
      ) {
        return false;
      }
      if (Objects.isNull(word)
          || word.isBlank()
          || word.length() > 15
          || word.length() > boardRows * boardCols
      ) {
        return false;
      }
      return true;
    }

    boolean dfs(final int m, final int n, final int index) {
      if (index == word.length()) {
        return true;
      }
      if (m < 0 || m >= boardRows
          || n < 0 || n >= boardCols
          || board[m][n] != word.charAt(index)
      ) {
        return false;
      }
      //System.out.printf("%d, %d, %d, %c%n", m, n, index, board[m][n]);
      var temp = board[m][n];
      board[m][n] = '#';
      int[][] adjacentCells = {
          {m + 1, n},
          {m - 1, n},
          {m, n + 1},
          {m, n - 1}
      };
      var found = false;
      for (var cell : adjacentCells) {
        found = found || dfs(cell[0], cell[1], index + 1);
      }
      board[m][n] = temp;
      return found;
    }

    public boolean exist(final char[][] board, final String word) {
      this.board = board;
      this.word = word;
      if (!validArgs()) {
        return false;
      }
      var boardCounter = new HashMap<Character, Integer>();
      for (var row : board) {
        for (var element : row) {
          boardCounter.put(element, boardCounter.getOrDefault(element, 0) + 1);
        }
      }
      var boardSet = boardCounter.keySet();
      var wordCharArray = word
          .chars()
          .mapToObj(c -> (char) c)
          .toArray();
      var wordSet = Arrays
          .stream(wordCharArray)
          .collect(Collectors.toSet());
      if (!boardSet.containsAll(wordSet)) {
        return false;
      }
      if (boardCounter.get(wordCharArray[0]) > boardCounter.get(wordCharArray[word.length() - 1])) {
        this.word = new StringBuffer(word)
            .reverse()
            .toString();
      }
      for (int m = 0; m < boardRows; m++) {
        for (int n = 0; n < boardCols; n++) {
          if (this.word.charAt(0) != board[m][n]) {
            continue;
          }
          if (dfs(m, n, 0)) {
            return true;
          }
        }
      }
      return false;
    }
  }

  // use the annotation below to 'no cover'
  @lombok.Generated
  public static void main(String[] args) {
    char[][] board = {{'A', 'B', 'C', 'E'}, {'S', 'F', 'C', 'S'}, {'A', 'D', 'E', 'E'}};
    String word = "ABCCED";
    boolean isPassed = new LeetCode79.Solution().exist(board, word) == true;
    System.out.printf("Is passed: %b", isPassed);
    assert isPassed;
  }
}
