package io.petesong.algorithms;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;


class TreeNodeTest {
  @Test
  void shouldReturnInstanceWithoutArgument() {
    TreeNode node = new TreeNode();
    Assertions.assertNotNull(node);
  }

  @Test
  void shouldReturnInstanceWithThreeArguments() {
    TreeNode node = new TreeNode(0, null, null);
    Assertions.assertNotNull(node);
  }

}
