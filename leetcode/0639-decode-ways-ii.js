/** https://leetcode.com/problems/decode-ways-ii/submissions/983705526/
 * @param {string} s
 * @return {number}
 */
const numDecodings = (s) => {
    const n = s.length
    const MOD = 10 ** 9 + 7

    const dp = Array(n + 2).fill(0)
    dp[0] = 1
    dp[1] = 1

    for (let i = 0; i < n; i++) {
        if (s[i] === '*') {
            dp[i + 2] = dp[i + 1] * 9

            if (s[i - 1] === '1' || s[i - 1] === '*') {
                dp[i + 2] += dp[i] * 9
            }
            if (s[i - 1] === '2' || s[i - 1] === '*') {
                dp[i + 2] += dp[i] * 6
            }
        }
        else {
            if (s[i] !== '0') {
                dp[i + 2] = dp[i + 1]
            }

            if (s[i - 1] === '1' || s[i - 1] === '*') {
                dp[i + 2] += dp[i]
            }
            if ((s[i - 1] === '2' || s[i - 1] === '*') && s[i] < '7') {
                dp[i + 2] += dp[i]
            }
        }
        dp[i + 2] %= MOD
    }

    return dp[n + 1]
}
