// https://leetcode.com/problems/word-ladder-ii/submissions/1006911335/

const isAdjacent = (firstWord, secondWord) => {
    const n = firstWord.length

    let d = 0
    for (let i = 0; i < n; i++) {
        if (firstWord[i] !== secondWord[i]) {
            if (d > 0) {
                return false
            }

            d += 1
        }
    }

    return d === 1
}

const buildGraph = (beginWord, endWord, words) => {
    const nodes = [beginWord, ...words].map(word => ({
        word: word,
        edges: [],
        d: -1,
    }))

    let endNode = nodes[nodes.length - 1];

    for (let i = 0; i < nodes.length - 1; i++) {
        for (let j = i + 1; j < nodes.length; j++) {
            if (isAdjacent(nodes[i].word, nodes[j].word)) {
                nodes[i].edges.push(nodes[j])
                nodes[j].edges.push(nodes[i])
            }

            if (nodes[i].word === endWord) {
                endNode = nodes[i]
            }
        }
    }

    const queue = [endNode]
    endNode.d = 0

    while (queue.length > 0) {
        const top = queue.shift()
        for (const node of top.edges) {
            if (node.d === -1) {
                node.d = top.d + 1
                queue.push(node)
            }
        }
    }

    return nodes[0]
}

const traverse = (currentNode) => {
    if (currentNode.d === 0) {
        return [
            [currentNode.word]
        ]
    }

    const totalPaths = []
    for (const nextNode of currentNode.edges) {
        if (nextNode.d !== currentNode.d - 1) {
            continue
        }

        const paths = traverse(nextNode)

        for (const path of paths) {
            totalPaths.push([currentNode.word, ...path])
        }
    }

    return totalPaths
}

/**
 * @param {string} beginWord
 * @param {string} endWord
 * @param {string[]} wordList
 * @return {string[][]}
 */
const findLadders = (beginWord, endWord, wordList) => {
    const endWordInWordList = wordList.includes(endWord)

    if (!endWordInWordList) {
        return []
    }

    const beginNode = buildGraph(beginWord, endWord, wordList)

    if (beginNode.d === -1) {
        return []
    }

    return traverse(beginNode)
}
