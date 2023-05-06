// https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/submissions/945482882/

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var numSubseq = function(nums, target) {
    const n = nums.length
    const MOD = 10 ** 9 + 7

    nums.sort((a, b) => a - b)

    const pow = Array(n)
    pow[0] = 1

    for (let i = 1; i < n; i++) {
        pow[i] = (pow[i - 1] * 2) % MOD
    }

    let left = 0
    let right = n - 1
    let count = 0
    while (left <= right) {
        if (nums[left] + nums[right] <= target) {
            count += pow[right - left]
            count %= MOD
            left++
        }
        else {
            right--
        }
    }

    return count
}