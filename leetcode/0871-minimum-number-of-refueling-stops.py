# https://leetcode.com/submissions/detail/781599897/

from heapq import heappush, heappop


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        stations.append([target, 0])
        n = len(stations)

        dist = 0
        fuel = startFuel
        past_stations = []
        refuels = 0

        for i in range(n):
            location = stations[i][0]
            capacity = stations[i][1]

            while len(past_stations) > 0 and dist + fuel < location:
                fuel += -heappop(past_stations)
                refuels += 1

            if dist + fuel >= location:
                heappush(past_stations, -capacity)
                fuel -= location - dist
                dist = location
            else:
                return -1

        return refuels
