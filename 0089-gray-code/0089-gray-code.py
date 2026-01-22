from typing import List

class Solution:
    def grayCode(self, n: int) -> List[int]:
        result = [0]
        
        for i in range(n):
            # Reflect the current list and add 1 << i to the reflected numbers
            result += [x | (1 << i) for x in reversed(result)]
        
        return result
