# https://leetcode.com/submissions/detail/705791943/

from math import inf


class Vertex:
    def __init__(self):
        self.time = inf
        self.edges = list()


class Edge:
    def __init__(self, dest, time):
        self.dest = dest
        self.time = time



class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = [Vertex() for _ in range(n)]

        for time in times:
            u, v, w = time
            g[u - 1].edges.append(Edge(g[v - 1], w))

        g[k - 1].time = 0
        s = set(g)

        while len(s) > 0:
            v_min = min(s, key=lambda v: v.time)
            s.remove(v_min)
            for e in v_min.edges:
                e.dest.time = min(e.dest.time, v_min.time + e.time)

        v_time_max = max(g, key=lambda v: v.time).time

        return v_time_max if v_time_max is not inf else -1
