class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=[[0] * 9 for _ in range(9)]
        cols=[[0] * 9 for _ in range(9)]
        squares=[[0] * 9 for _ in range(9)]
        for row in range(9):
            for col in range(9):
                if board[row][col].isalnum():
                    to_int=int(board[row][col])
                    if rows[row][to_int-1]!=0:
                        return False
                    else:
                        rows[row][to_int-1]=1

                    if cols[col][to_int-1]!=0:
                        return False
                    else:
                        cols[col][to_int-1]=1
                    if squares[row//3 + col//3 + 2*(row//3)][to_int-1]!=0:
                        return False
                    else:
                        squares[row//3 + col//3 + 2*(row//3)][to_int-1]=1
        return True
                    
                    
                    

        