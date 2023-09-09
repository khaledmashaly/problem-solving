// https://leetcode.com/problems/palindrome-partitioning-ii/submissions/1044836660/

const isPalindrome = (s) => {
    for (let i = 0; i < Math.floor(s.length / 2); i++) {
        if (s[i] !== s[s.length - i - 1]) {
            return false
        }
    }

    return true
}

const minPalindrome = (s, i, memo) => {
    if (i === s.length) {
        return 0
    }

    if (i in memo) {
        return memo[i]
    }

    let ans = Number.MAX_SAFE_INTEGER

    for (let j = i; j < s.length; j++) {
        if (isPalindrome(s.slice(i, j + 1))) {
            const palindrome = minPalindrome(s, j + 1, memo)
            ans = Math.min(ans, palindrome + 1)
        }
    }

    memo[i] = ans
    return ans
}

/**
 * @param {string} s
 * @return {number}
 */
const minCut = (s) => {
    return minPalindrome(s, 0, {}) - 1
}