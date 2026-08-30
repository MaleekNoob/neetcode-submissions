from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        row_seen = defaultdict(set)
        col_seen = defaultdict(set)
        grid_seen = defaultdict(set)

        for x, row in enumerate(board):
            for y, val in enumerate(row):

                if val == '.':
                    continue

                sub_grid = (x // 3, y // 3)

                if val in  row_seen[x] or val in col_seen[y] or val in grid_seen[sub_grid]:
                    return False

                row_seen[x].add(val)
                col_seen[y].add(val)
                grid_seen[sub_grid].add(val)

        return True
        