// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/submissions/988578456/

const lca = (root, p, q) => {
    if (root === null) {
        return {}
    }

    const left = lca(root.left, p, q)

    if (left.ans) {
        return { ans: left.ans }
    }

    const right = lca(root.right, p, q)

    if (right.ans) {
        return { ans: right.ans }
    }

    const pFound = left.pFound || right.pFound || root.val === p.val
    const qFound = left.qFound|| right.qFound || root.val === q.val

    if (pFound && qFound) {
        return { ans: root }
    }

    return {
        pFound,
        qFound,
    }
}

/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {TreeNode}
 */
const lowestCommonAncestor = (root, p, q) => {
    const ans = lca(root, p, q)
    return ans.ans
}