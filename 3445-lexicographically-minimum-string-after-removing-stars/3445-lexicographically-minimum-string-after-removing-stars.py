class Solution:
    def clearStars(self, s: str) -> str:
        stack = []  # to keep characters
        positions = [[] for _ in range(26)]  # to track positions of each letter (a-z)

        for i, ch in enumerate(s):
            if ch != '*':
                stack.append(ch)
                positions[ord(ch) - ord('a')].append(len(stack) - 1)
            else:
                # Find smallest letter available in stack
                for j in range(26):
                    if positions[j]:
                        idx = positions[j].pop()
                        stack[idx] = None  # mark as deleted
                        break  # found and deleted smallest char
        # Build final string without None and '*'
        return ''.join(ch for ch in stack if ch is not None)
