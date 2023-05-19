/** https://leetcode.com/problems/maximum-performance-of-a-team/submissions/953433697/
 * @param {number} n
 * @param {number[]} speed
 * @param {number[]} efficiency
 * @param {number} k
 * @return {number}
 */
const maxPerformance = (n, speed, efficiency, k) => {
    const MOD = BigInt(10 ** 9 + 7)
    const engs = _.orderBy(_.zip(efficiency, speed), ['0'], ['desc'])
    const selected = new MinPriorityQueue()
    let speeds = 0
    let maxPerf = 0n

    for (const [e, s] of engs) {
        if (selected.size() === k) {
            speeds -= selected.dequeue().element
        }

        selected.enqueue(s)
        speeds += s

        const currentPerf = BigInt(speeds) * BigInt(e)

        if (currentPerf > maxPerf) {
            maxPerf = currentPerf
        }
    }

    return maxPerf % MOD
}