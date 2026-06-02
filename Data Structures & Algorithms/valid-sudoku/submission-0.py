class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r = set()
        c = set()
        s = set()
        for i in range(9):
            for j in range(9):
                row = board[i][j]
                col = board[j][i]
                if row.isdigit():
                    if row in r:
                        return False
                    r.add(row)
                if col.isdigit():
                    if col in c:
                        return False
                    c.add(col)
            r.clear()
            c.clear()

        # 1. Loop through the row origins of the 3x3 blocks (0, 3, 6)
        for block_row in range(0, 9, 3):
            # 2. Loop through the column origins of the 3x3 blocks (0, 3, 6)
            for block_col in range(0, 9, 3):
                # 3. Traverse inside the current 3x3 sub-matrix
                for i in range(3):
                    for j in range(3):
                        row = block_row + i
                        col = block_col + j
                        val = board[row][col]
                        if val.isdigit():
                            if val in s:
                                return False
                            s.add(val)
                s.clear()
        return True
