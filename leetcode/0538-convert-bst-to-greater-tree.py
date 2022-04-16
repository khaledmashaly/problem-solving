# https://leetcode.com/submissions/detail/681614667/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        greater_sum = 0
        visited = set()
        stack = [root]
        while stack:
            top = stack[-1]
            if top.right and top.right not in visited:
                stack.append(top.right)
                continue

            if top not in visited:
                greater_sum += top.val
                top.val = greater_sum
                visited.add(top)

            if top.left and top.left not in visited:
                stack.append(top.left)
                continue

            stack.pop()

        return root
