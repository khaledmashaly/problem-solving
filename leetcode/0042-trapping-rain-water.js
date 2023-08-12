/** https://leetcode.com/problems/trapping-rain-water/submissions/1019241061/
 * @param {number[]} heights
 * @return {number}
 */
const trap = (heights) => {
    const s = []
    let water = 0
    for (let i = 0; i < heights.length; i++) {
        let dec = 0
        while (s.length > 0) {
            const top = s[s.length - 1]
            const width = i - top - 1
            const height = Math.min(heights[i] - dec, heights[top] - dec)
            water += width * height
            dec += height

            if (heights[top] > heights[i]) {
                break
            }

            s.pop()
        }

        s.push(i)
    }

    return water
}
