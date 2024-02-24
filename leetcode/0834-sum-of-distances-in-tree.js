// https://leetcode.com/problems/sum-of-distances-in-tree/submissions/1185105541

const dfs1 = (graph, current, parent, count, res) => {
    for (const child of graph[current]) {
        if (child === parent) {
            continue
        }

        dfs1(graph, child, current, count, res)
        count[current] += count[child]
        res[current] += res[child] + count[child]
    }
}

const dfs2 = (graph, current, parent, count, res) => {
    for (const child of graph[current]) {
        if (child === parent) {
            continue
        }

        res[child] = res[current] - count[child] + graph.length - count[child]
        dfs2(graph, child, current, count, res)
    }
}

const calculateSumOfDistances = (graph) => {
    const count = Array(graph.length).fill(1)
    const res = Array(graph.length).fill(0)

    dfs1(graph, 0, -1, count, res)
    dfs2(graph, 0, -1, count, res)

    return res
}

/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {number[]}
 */
const sumOfDistancesInTree = (n, edges) => {
    const g = Array(n).fill().map(_ => [])

    for (const edge of edges) {
        g[edge[0]].push(edge[1])
        g[edge[1]].push(edge[0])
    }

    return calculateSumOfDistances(g)
}
