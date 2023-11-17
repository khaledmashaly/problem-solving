/** https://leetcode.com/problems/maximum-profit-in-job-scheduling/submissions/1100973491/
 * @param {number[]} startTime
 * @param {number[]} endTime
 * @param {number[]} profit
 * @return {number}
 */
const jobScheduling = (startTime, endTime, profit) => {
    [startTime, endTime, profit] = _.unzip(_.sortBy(_.zip(startTime, endTime, profit), ['0']))
    const n = startTime.length
    const tab = new Array(n + 1).fill(0)

    for (let i = n - 1; i >= 0; i--) {
        const next = _.sortedIndex(startTime, endTime[i])
        tab[i] = Math.max(profit[i] + tab[next], tab[i + 1])
    }

    return tab[0]
}