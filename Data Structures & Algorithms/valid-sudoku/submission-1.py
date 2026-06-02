class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r = set()
        c = set()
        s = set()
        for i in range(9):
            for j in range(9):
                row = board[i][j]
                col = board[j][i]
                box_row = (i // 3) * 3 + j // 3
                box_col = (i % 3) * 3 + j % 3
                val = board[box_row][box_col]
                if row.isdigit():
                    if row in r:
                        return False
                    r.add(row)
                if col.isdigit():
                    if col in c:
                        return False
                    c.add(col)
                if val.isdigit():
                    if val in s:
                        return False
                    s.add(val)
            r.clear()
            c.clear()
            s.clear()
      
        return True
