class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(row,col,board,word,ind):
            if(ind == len(word)):
                return True 
            for r,c in [[-1,0],[1,0],[0,-1],[0,1]]:
                nr = r+row 
                nc = c+col 
                if(nr>=0 and nr<n and nc>=0 and nc<m and board[nr][nc] == word[ind]):
                    board[nr][nc] = '.'
                    if(backtrack(nr,nc,board,word,ind+1)):
                        return True 
                    board[nr][nc] = word[ind] 
            return False 
        n = len(board) # no of rows 
        m = len(board[0]) # no of cols
        for row in range(0,n):
            for col in range(0,m):
                if(board[row][col] == word[0]): 
                    board[row][col] = "." 
                    if(backtrack(row,col,board,word,1)):
                        return True 
                    board[row][col] = word[0]
        return False