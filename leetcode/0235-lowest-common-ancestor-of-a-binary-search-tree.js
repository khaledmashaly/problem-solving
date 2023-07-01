/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */

/** https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/submissions/983702959/
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {TreeNode}
 */
const lowestCommonAncestor = (root, p, q) => {
    const a = Math.min(p.val, q.val)
    const b = Math.max(p.val, q.val)

    while (!(root.val >= a && root.val <= b)) {
        if (root.val < a) {
            root = root.right
        }
        else {
            root = root.left
        }
    }

    return root
}
