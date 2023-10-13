// https://leetcode.com/problems/longest-uncommon-subsequence-ii/submissions/1074478934/

const isSubString = (a, b) => {
    if (a.length < b.length) {
        return false
    }

    let j = 0

    for (let i = 0; i < a.length; i++) {
        if (j === b.length) {
            return true
        }

        if (a[i] === b[j]) {
            j += 1
        }
    }

    return j === b.length
}


/**
 * @param {string[]} strs
 * @return {number}
 */
const findLUSlength = (strs) => {
    let ans = -1

    for (let i = 0; i < strs.length; i++) {
        let isUncommon = true

        for (let j = 0; j < strs.length; j++) {
            if (i === j) {
                continue
            }

            if (isSubString(strs[j], strs[i])) {
                isUncommon = false
                break
            }
        }

        if (isUncommon && strs[i].length > ans) {
            ans = strs[i].length
        }
    }

    return ans
}