from collections import defaultdict
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                # Skip empty cells
                if val == ".":
                    continue
                
                # Check if value already exists in row, col, or 3x3 box
                box_key = (r // 3, c // 3)
                if val in rows[r] or val in cols[c] or val in boxes[box_key]:
                    return False
                
                # Add value to respective sets
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_key].add(val)

        return True