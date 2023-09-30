// https://leetcode.com/problems/sudoku-solver/submissions/1063266561/
const canExtend = (board, r, c, item) => {
    // check row
    for (let j = 0; j <= 8; j++) {
        if (board[r][j] === item) {
            return false
        }
    }

    // check col
    for (let i = 0; i <= 8; i++) {
        if (board[i][c] === item) {
            return false
        }
    }

    // check sub box
    const rStart = Math.floor(r / 3) * 3
    const rEnd = rStart + 2
    const cStart = Math.floor(c / 3) * 3
    const cEnd = cStart + 2

    for (let i = rStart; i <= rEnd; i++) {
        for (let j = cStart; j <= cEnd; j++) {
            if (board[i][j] === item) {
                return false
            }
        }
    }

    return true
}

const solve = (board, r, c) => {
    for (let i = 0; i <= 8; i++) {
        for (let j = 0; j <= 8; j++) {
            if (board[i][j] !== '.') {
                continue
            }

            for (let x = 1; x <= 9; x++) {
                if (canExtend(board, i, j, `${x}`)) {
                    board[i][j] = `${x}`
                    if (solve(board, i, j)) {
                        return true
                    }
                    board[i][j] = '.'
                }
            }

            return false
        }
    }

    return true
}


/**
 * @param {character[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */
const solveSudoku = (board) => {
    solve(board, 0, 0)
}
