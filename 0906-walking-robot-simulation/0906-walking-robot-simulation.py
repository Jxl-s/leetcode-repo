class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        max_dist = 0
        obstacles_set = set()
        for x, y in obstacles:
            obstacles_set.add((x, y))

        direction = 0 # clockwise, starting from top
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x, y = 0, 0

        for cmd in commands:
            if cmd == -2:
                direction -= 1
                if direction == -1:
                    direction = 3

            elif cmd == -1:
                direction += 1
                if direction == 4:
                    direction = 0

            else:
                for k in range(cmd):
                    move = directions[direction]

                    nx = x + move[0]
                    ny = y + move[1]

                    if (nx, ny) in obstacles_set:
                        break

                    x = nx
                    y = ny
                    max_dist = max(max_dist, x*x + y*y)

        return max_dist