# https://leetcode.com/submissions/detail/789680374/


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        current_level = [root]

        ans = []
        while current_level:
            next_level = []

            current_sum = 0
            current_count = 0

            for node in current_level:
                current_sum += node.val
                current_count += 1

                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            current_level = next_level
            ans.append(current_sum / current_count)

        return ans
