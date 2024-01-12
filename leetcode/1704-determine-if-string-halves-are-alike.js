/** https://leetcode.com/problems/determine-if-string-halves-are-alike/submissions/1144270421
 * @param {string} s
 * @return {boolean}
 */
const halvesAreAlike = (s) => {
    const vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    let i = 0
    const mid = s.length / 2
    let firstCount = 0
    let secondCount = 0

    while (i < mid) {
        if (vowels.includes(s[i])) {
            firstCount += 1
        }
        i += 1
    }

    while (i < s.length) {
        if (vowels.includes(s[i])) {
            secondCount += 1
        }
        i += 1
    }

    return firstCount == secondCount
}
