# https://leetcode.com/submissions/detail/797461016/


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        s = [root]

        ans = []
        visited = set()
        while len(s) > 0:
            top = s[-1]

            if top.left is not None and top.left not in visited:
                s.append(top.left)
                continue

            if top not in visited:
                ans.append(top.val)
                visited.add(top)

            if top.right is not None and top.right not in visited:
                s.append(top.right)
                continue

            s.pop()

        return ans
