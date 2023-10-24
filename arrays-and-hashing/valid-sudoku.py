def isValidSudoku(self, board: List[List[str]]) -> bool:
    # Applying hashsets, where each row/column/square corresponds to a set
    # Eg. {row1/col1/square1 : row1_set/col1_set/sq1_set}
    # Set will contain only non-duplicate values
    row = collections.defaultdict(set)
    column = collections.defaultdict(set)
    square = collections.defaultdict(set) # 9x9 sudoku will have 3x3 squares
    # (r, c) cell will belong to (r/3, c/3) square
    # Eg, 2,2 cell will belong to 2/3, 2/3 = (0, 0) = first square
    for r in range(9):
        for c in range(9):
            if(board[r][c] == "."):
                continue
            
            if(board[r][c] in row[r] or
                board[r][c] in column[c] or
                board[r][c] in square[(r // 3, c // 3)]):
                return False
            
            row[r].add(board[r][c])
            column[c].add(board[r][c])
            square[(r // 3, c // 3)].add(board[r][c])
        
    return True