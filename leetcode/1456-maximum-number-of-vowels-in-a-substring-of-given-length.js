// https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/submissions/944908140/

/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
const maxVowels = (s, k) => {
    const n = s.length
    const vowels = ['a', 'e', 'i', 'o', 'u']
    let count = 0
    let maxCount = 0

    for (let i = 0; i < n; i++) {
        if (vowels.includes(s[i])) {
            count += 1
        }

        if (i - k >= 0 && vowels.includes(s[i - k])) {
            count -= 1
        }

        maxCount = Math.max(maxCount, count)
    }

    return maxCount
}
