// https://leetcode.com/problems/similar-string-groups/submissions/941743589/

const similar = (str1, str2) => {
    let d = 0
    const n = str1.length

    for (let i = 0; i < n; i++) {
        if (str1[i] !== str2[i]) {
            d++
        }
    }

    return d === 0 || d === 2
}

const getRoot = (parent, i) => {
    let p = i

    while (parent[p] !== p) {
        p = parent[p]
    }

    return p
}

/**
 * @param {string[]} strs
 * @return {number}
 */
var numSimilarGroups = function(strs) {
    const n = strs.length
    const parent = strs.map((_, i) => i)

    for (let i = 0; i < n - 1; i++) {
        for (let j = i + 1; j < n; j++) {
            if (similar(strs[i], strs[j])) {
                pi = getRoot(parent, i)
                pj = getRoot(parent, j)
                if (pi !== pj) {
                    parent[pj] = pi
                }
            }
        }
    }

    let groups = 0
    for (let i = 0; i < n; i++) {
        if (i === parent[i]) {
            groups++
        }
    }

    return groups
}
