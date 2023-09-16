/** https://leetcode.com/problems/array-of-doubled-pairs/submissions/1051050480/
 * @param {number[]} arr
 * @return {boolean}
 */
const canReorderDoubled = (arr) => {
    const count = {}

    for (const num of arr) {
        count[num] = num in count ? count[num] + 1 : 1
    }

    arr.sort((a, b) => Math.abs(a) - Math.abs(b))

    for (const num of arr) {
        if (count[num] === 0) {
            continue
        }

        if (!((num * 2) in count) || count[num * 2] === 0) {
            return false
        }

        count[num] -= 1
        count[num * 2] -= 1
    }

    return true
}
