# https://leetcode.com/submissions/detail/744625066/


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        ans = []
        current_level = [root]

        while current_level:
            ans.append(current_level[-1].val)

            next_level = []
            for node in current_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            current_level = next_level

        return ans
