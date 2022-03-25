# https://leetcode.com/submissions/detail/667066725/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda cost: cost[0] - cost[1])

        n = len(costs)
        min_cost = 0
        for i in range(n // 2):
            min_cost += costs[i][0] + costs[n - i - 1][1]

        return min_cost
