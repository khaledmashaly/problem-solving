/** https://leetcode.com/problems/longest-increasing-subsequence/submissions/967380642/
* @param {number[]} nums
* @return {number}
*/
const lengthOfLIS = (nums) => {
    const n = nums.length
    const dp = Array(n).fill(1)

    let ans = 1
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < i; j++) {
            if (nums[i] > nums[j]) {
                dp[i] = Math.max(dp[i], dp[j] + 1)
            }
        }

        ans = Math.max(dp[i], ans)
    }

    return ans
}