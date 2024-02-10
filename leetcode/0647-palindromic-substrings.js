// https://leetcode.com/problems/palindromic-substrings/submissions/1171766727

const countPalindromes = (str, l, r) => {
    let count = 0

    while (l >= 0 && r < str.length && str[l] === str[r]) {
        count += 1
        r += 1
        l -= 1
    }

    return count
}

/**
 * @param {string} s
 * @return {number}
 */
const countSubstrings = (str) => {
    let count = 0

    for (let i = 0; i < str.length; i++) {
        const even = countPalindromes(str, i, i + 1)
        const odd = countPalindromes(str, i - 1, i + 1)
        count += even + odd + 1
    }

    return count
}
