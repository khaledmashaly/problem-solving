# https://leetcode.com/submissions/detail/747294194/

class Solution:
    def build_sub_tree(self, preorder, inorder, root_index, inorder_map, start, end):
        if start >= end:
            return None, root_index

        root = TreeNode()
        root.val = preorder[root_index]
        root_inorder_index = inorder_map[root.val]


        left, root_index = self.build_sub_tree(preorder, inorder, root_index + 1, inorder_map, start, root_inorder_index)
        right, root_index = self.build_sub_tree(preorder, inorder, root_index, inorder_map, root_inorder_index + 1, end)

        root.left = left
        root.right = right

        return root, root_index

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {}
        for i, node in enumerate(inorder):
            inorder_map[node] = i

        root, _ = self.build_sub_tree(preorder, inorder, 0, inorder_map, 0, len(inorder))

        return root
