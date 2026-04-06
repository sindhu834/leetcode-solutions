class Solution:
    def robotSim(self, commands, obstacles):
        obstacles_set = set(map(tuple, obstacles))

        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        x, y = 0, 0
        d = 0
        max_dist = 0

        for cmd in commands:
            if cmd == -2:  # turn left
                d = (d + 3) % 4
            elif cmd == -1:  # turn right
                d = (d + 1) % 4
            else:
                for _ in range(cmd):
                    nx = x + dirs[d][0]
                    ny = y + dirs[d][1]

                    if (nx, ny) in obstacles_set:
                        break

                    x, y = nx, ny
                    max_dist = max(max_dist, x*x + y*y)

        return max_dist