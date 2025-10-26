from collections import deque

class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(0, 1, 0)])  # (position, speed, moves)
        visited = set([(0, 1)])     # visited states

        while queue:
            position, speed, moves = queue.popleft()

            # ✅ Reached the target
            if position == target:
                return moves

            # ---- Option 1: Accelerate ----
            new_pos = position + speed
            new_speed = speed * 2
            if (new_pos, new_speed) not in visited and abs(new_pos) <= 2 * target:
                visited.add((new_pos, new_speed))
                queue.append((new_pos, new_speed, moves + 1))

            # ---- Option 2: Reverse ----
            rev_speed = -1 if speed > 0 else 1
            if (position, rev_speed) not in visited:
                visited.add((position, rev_speed))
                queue.append((position, rev_speed, moves + 1))
