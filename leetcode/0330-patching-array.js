/** https://leetcode.com/problems/patching-array/submissions/1116013197/
 * @param {number[]} nums
 * @param {number} n
 * @return {number}
 */
const minPatches = (nums, n) => {
    let sum = 0
    let i = 0
    let ans = 0

    while (sum < n) {
        if (i < nums.length && nums[i] <= sum + 1) {
            sum += nums[i]
            i += 1
        }
        else {
            sum += sum + 1
            ans += 1
        }
    }

    return ans
}