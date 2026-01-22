from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(i, j, index):
            # Check if all letters matched
            if index == len(word):
                return True
            # Check boundaries and current letter
            if i < 0 or i >= rows or j < 0 or j >= cols or board[i][j] != word[index]:
                return False

            # Mark the cell as visited
            temp = board[i][j]
            board[i][j] = '#'

            # Explore 4 directions
            found = (dfs(i+1, j, index+1) or
                     dfs(i-1, j, index+1) or
                     dfs(i, j+1, index+1) or
                     dfs(i, j-1, index+1))

            # Restore the cell
            board[i][j] = temp
            return found

        # Start DFS from each cell
        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True
        return False
