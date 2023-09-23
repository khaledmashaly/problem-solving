// https://leetcode.com/problems/remove-boxes/submissions/1057295108/
const maxScore = (l, r, k, boxes, memo) => {
    if (l > r) {
        return 0
    }

    if (l === r) {
        return (k + 1) * (k + 1)
    }

    if (memo[l][r][k] !== 0) {
        return memo[l][r][k]
    }

    memo[l][r][k] = (k + 1) * (k + 1) + maxScore(l + 1, r, 0, boxes, memo)

    for (let i = l + 1; i <= r; i++) {
        if (boxes[i] === boxes[l]) {
            memo[l][r][k] = Math.max(memo[l][r][k], maxScore(l + 1, i - 1, 0, boxes, memo) + maxScore(i, r, k + 1, boxes, memo))
        }
    }

    return memo[l][r][k]
}

/**
 * @param {number[]} boxes
 * @return {number}
 */
const removeBoxes = (boxes) => {
    const n = boxes.length
    const memo = Array(n).fill().map(_ => Array(n).fill().map(_ => Array(n).fill(0)))

    return maxScore(0, n - 1, 0, boxes, memo)
};