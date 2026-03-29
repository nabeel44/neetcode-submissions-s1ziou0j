class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        grids = defaultdict(set)
        for row in range(len(board)):
            for col in range(len(board)):
                val = board[row][col]
                if val == '.':
                    continue
                grid = (row // 3, col // 3)
                if val in rows[row] or val in cols[col] or val in grids[grid]:
                    return False
                else:
                    rows[row].add(val)
                    cols[col].add(val)
                    grids[grid].add(val)
        return True

        