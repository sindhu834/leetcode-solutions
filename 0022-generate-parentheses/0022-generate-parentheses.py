class Solution:
    def generateParenthesis(self, n: int):
        result = []

        def backtrack(curr, open_cnt, close_cnt):
            # If the current string is complete
            if len(curr) == 2 * n:
                result.append(curr)
                return
            
            # Add '(' if possible
            if open_cnt < n:
                backtrack(curr + "(", open_cnt + 1, close_cnt)
            
            # Add ')' if it keeps string valid
            if close_cnt < open_cnt:
                backtrack(curr + ")", open_cnt, close_cnt + 1)

        backtrack("", 0, 0)
        return result
