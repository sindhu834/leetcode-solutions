class Solution:
    def validateStackSequences(self, pushed, popped):
        stack = []
        j = 0  # pointer for popped list

        for x in pushed:
            stack.append(x)  # simulate push
            # keep popping while top of stack == popped[j]
            while stack and j < len(popped) and stack[-1] == popped[j]:
                stack.pop()
                j += 1
        
        # if all popped elements are processed, it's valid
        return j == len(popped)
