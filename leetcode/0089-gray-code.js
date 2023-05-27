/** https://leetcode.com/problems/gray-code/submissions/957685317/
 * @param {number} n
 * @return {number[]}
 */
const grayCode = (n) => {
    const m = 2 ** n
    const numbers = Array(m).fill(0)

    for (let i = 0; i < n; i++) {

        const s = 2 ** i
        for (let j = s; j < m; j += s * 4) {

            const e = Math.min(j + s * 2, m)
            for (let k = j; k < e; k++) {
                numbers[k] |= 1 << i
            }
        }
    }

    return numbers
}
