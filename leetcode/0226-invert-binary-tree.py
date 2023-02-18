# https://leetcode.com/problems/invert-binary-tree/submissions/900466372/

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        current_level = [root]
        while len(current_level) > 0:
            next_level = []
            for node in current_level:
                node.left, node.right = node.right, node.left
                if node.left is not None:
                    next_level.append(node.left)
                if node.right is not None:
                    next_level.append(node.right)
            current_level = next_level

        return root
