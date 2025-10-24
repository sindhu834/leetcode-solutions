class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge case: if only 1 row or fewer characters than rows
        if numRows == 1 or numRows >= len(s):
            return s

        # Create an array to hold strings for each row
        rows = ['' for _ in range(numRows)]
        current_row = 0
        going_down = False  # Direction flag

        # Traverse each character in the string
        for char in s:
            rows[current_row] += char  # Add character to current row

            # Change direction when hitting top or bottom row
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down

            # Move to next row based on direction
            current_row += 1 if going_down else -1

        # Join all rows together
        return ''.join(rows)
