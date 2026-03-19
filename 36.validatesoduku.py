
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
                #hashset where key is gonna be the colum number 
        cols=collections.defaultdict(set)

                # hashset where value is gonna be the raw number
        rows=collections.defaultdict(set)

        # hashset witht the squares 
        # key = (r/3,c/3)
        squares=collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c]==".":
                   continue
                #    if exits in rows or columns or in current square that we are in
                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r//3,c//3)]):
                    return False
        
                cols[c].add(board[r][c])   
                rows[r].add(board[r][c]) 
                squares[(r//3,c//3)].add(board[r][c])
        return True       



       
    
